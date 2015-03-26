# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(to='core.Category', null=True)),
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
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('times_ordered', models.IntegerField()),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('description', models.TextField()),
                ('nutritional_info', models.URLField()),
                ('is_vegetarian', models.BooleanField()),
                ('allergens', models.CharField(max_length=10, choices=[(b'PEANUT', b'Peanuts'), (b'GLUTEN', b'Gluten')])),
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
                ('menu_items', models.ManyToManyField(to='core.MenuItem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=2, choices=[(b'OP', b'Open'), (b'OC', b'Occupied'), (b'NR', b'Need refill'), (b'PL', b'Order placed')])),
                ('prev_status', models.CharField(max_length=2, choices=[(b'OP', b'Open'), (b'OC', b'Occupied'), (b'NR', b'Need refill'), (b'PL', b'Order placed')])),
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
    ]
