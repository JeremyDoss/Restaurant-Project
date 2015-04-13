# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, to='core.Category', null=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('is_manager', models.BooleanField(default=False)),
                ('passkey', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField()),
                ('message', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('in_stock', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subtotal', models.DecimalField(max_digits=10, decimal_places=2)),
                ('tax', models.DecimalField(max_digits=5, decimal_places=2)),
                ('tip', models.DecimalField(max_digits=5, decimal_places=2)),
                ('comped', models.BooleanField(default=False)),
                ('total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('split_ways', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('times_ordered', models.IntegerField()),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('description', models.TextField()),
                ('image', models.URLField(blank=True)),
                ('nutritional_info', models.URLField(blank=True)),
                ('calories', models.IntegerField()),
                ('fat_grams', models.IntegerField()),
                ('sodium_mg', models.IntegerField()),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('in_stock', models.BooleanField(default=True)),
                ('allergens', models.CharField(default=b'NONE', max_length=10, choices=[(b'NONE', b'None'), (b'PEANUT', b'Peanuts'), (b'GLUTENFREE', b'Gluten-Free')])),
                ('category', models.ForeignKey(to='core.Category')),
                ('ingredients', models.ManyToManyField(to='core.Ingredient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True)),
                ('status', models.CharField(default=b'OP', max_length=2, choices=[(b'OP', b'Open'), (b'CL', b'Closed'), (b'RD', b'Ready to be served')])),
                ('menu_items', models.ManyToManyField(to='core.MenuItem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Split',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('invoice', models.ForeignKey(to='core.Invoice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'OP', max_length=2, choices=[(b'OP', b'Open'), (b'OC', b'Occupied'), (b'NR', b'Need refill'), (b'NA', b'Need assistance'), (b'PL', b'Order placed')])),
                ('prev_status', models.CharField(default=b'OP', max_length=2, choices=[(b'OP', b'Open'), (b'OC', b'Occupied'), (b'NR', b'Need refill'), (b'NA', b'Need assistance'), (b'PL', b'Order placed')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee', models.ForeignKey(to='core.Employee')),
                ('tables', models.ManyToManyField(to='core.Table')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.ForeignKey(to='core.Table'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='order',
            field=models.ForeignKey(to='core.Order'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedback',
            name='order',
            field=models.ForeignKey(to='core.Order'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cook',
            name='current_orders',
            field=models.ManyToManyField(to='core.Order', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cook',
            name='employee',
            field=models.ForeignKey(to='core.Employee'),
            preserve_default=True,
        ),
    ]
