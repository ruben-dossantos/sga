# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sga', '0005_auto_20151118_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'images/promotions', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='promotion',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='sga.Image', null=True),
        ),
    ]
