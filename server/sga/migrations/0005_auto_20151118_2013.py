# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sga', '0004_auto_20151118_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='user_type',
            field=models.IntegerField(blank=True, null=True, choices=[(2, b'Shopping Center Admin'), (3, b'Store Admin')]),
        ),
    ]
