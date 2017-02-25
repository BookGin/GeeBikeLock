# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlemap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bike',
            name='lng',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bike',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]
