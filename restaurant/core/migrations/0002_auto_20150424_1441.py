# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=512)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='allergens',
            field=models.CharField(default=b'NONE', max_length=10, choices=[(b'NONE', b'None'), (b'PEANUT', b'Peanuts'), (b'GLUTEN', b'Gluten')]),
            preserve_default=True,
        ),
    ]
