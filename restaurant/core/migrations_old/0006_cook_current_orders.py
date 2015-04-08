# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150406_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='cook',
            name='current_orders',
            field=models.ManyToManyField(to='core.Order', blank=True),
            preserve_default=True,
        ),
    ]
