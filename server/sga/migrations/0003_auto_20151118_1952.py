# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sga', '0002_auto_20151118_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AgeGroupPromotion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age_group', models.ForeignKey(to='sga.AgeGroup', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AreaBeacon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.ForeignKey(to='sga.Area', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
        migrations.CreateModel(
            name='AreaPromotion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.ForeignKey(to='sga.Area', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1)),
                ('age', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('promo_code', models.CharField(max_length=20, null=True, blank=True)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('link', models.CharField(max_length=200, null=True, blank=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('is_flash_promotion', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PromotionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TrackingArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('area', models.ForeignKey(to='sga.Area', on_delete=django.db.models.deletion.PROTECT)),
                ('device', models.ForeignKey(to='sga.Device', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
        migrations.AlterField(
            model_name='store',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='promotion',
            name='promotion_type',
            field=models.ForeignKey(to='sga.PromotionType', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='device',
            name='store',
            field=models.ForeignKey(to='sga.Store', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='beacon',
            name='store',
            field=models.ForeignKey(to='sga.Store', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='areapromotion',
            name='promotion',
            field=models.ForeignKey(to='sga.Promotion', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='areabeacon',
            name='beacon',
            field=models.ForeignKey(to='sga.Beacon', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='area',
            name='store',
            field=models.ForeignKey(to='sga.Store', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='agegrouppromotion',
            name='promotion',
            field=models.ForeignKey(to='sga.Promotion', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterUniqueTogether(
            name='areapromotion',
            unique_together=set([('area', 'promotion')]),
        ),
        migrations.AlterUniqueTogether(
            name='areabeacon',
            unique_together=set([('area', 'beacon')]),
        ),
        migrations.AlterUniqueTogether(
            name='agegrouppromotion',
            unique_together=set([('age_group', 'promotion')]),
        ),
    ]
