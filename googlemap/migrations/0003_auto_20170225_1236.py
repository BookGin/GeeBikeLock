# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlemap', '0002_auto_20170225_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='lat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='bike',
            name='lng',
            field=models.FloatField(default=0.0),
        ),
    ]
