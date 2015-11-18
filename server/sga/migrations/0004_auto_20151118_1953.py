# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sga', '0003_auto_20151118_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='age',
            field=models.IntegerField(),
        ),
    ]
