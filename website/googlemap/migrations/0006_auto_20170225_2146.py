# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlemap', '0005_bike_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='is_stolen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bike',
            name='moving_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bike',
            name='uid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bike',
            name='x',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='bike',
            name='y',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='bike',
            name='z',
            field=models.FloatField(default=0.0),
        ),
    ]
