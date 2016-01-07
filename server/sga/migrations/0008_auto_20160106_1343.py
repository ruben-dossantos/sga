# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sga', '0007_remove_device_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='agegroup',
            name='age_max',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agegroup',
            name='age_min',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
