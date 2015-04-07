# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
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
                ('order', models.ForeignKey(to='core.Order')),
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
                ('order', models.ForeignKey(to='core.Order')),
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
            model_name='cook',
            name='employee',
            field=models.ForeignKey(to='core.Employee'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'OP', max_length=2, choices=[(b'OP', b'Open'), (b'CL', b'Closed'), (b'RD', b'Ready to be served')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, to='core.Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='is_vegetarian',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='table',
            name='prev_status',
            field=models.CharField(default=b'OP', max_length=2, choices=[(b'OP', b'Open'), (b'OC', b'Occupied'), (b'NR', b'Need refill'), (b'NA', b'Need assistance'), (b'PL', b'Order placed')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='table',
            name='status',
            field=models.CharField(default=b'OP', max_length=2, choices=[(b'OP', b'Open'), (b'OC', b'Occupied'), (b'NR', b'Need refill'), (b'NA', b'Need assistance'), (b'PL', b'Order placed')]),
            preserve_default=True,
        ),
    ]
