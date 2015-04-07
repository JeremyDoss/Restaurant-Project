# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_menuitem_in_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='calories',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='fat_grams',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='sodium_mg',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='nutritional_info',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
