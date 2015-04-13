# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150405_0107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='allergens',
            field=models.CharField(default=b'NONE', max_length=10, choices=[(b'NONE', b'None'), (b'PEANUT', b'Peanuts'), (b'GLUTEN', b'Gluten')]),
            preserve_default=True,
        ),
    ]
