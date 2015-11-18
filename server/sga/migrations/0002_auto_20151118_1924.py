# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sga', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='user_type',
            field=models.IntegerField(choices=[(2, b'Shopping Center Admin'), (3, b'Store Admin')]),
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]
