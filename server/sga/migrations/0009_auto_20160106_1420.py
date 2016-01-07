# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sga', '0008_auto_20160106_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='discount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promotion',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
