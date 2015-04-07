# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150405_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='in_stock',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
