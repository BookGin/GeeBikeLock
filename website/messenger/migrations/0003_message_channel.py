# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-04 07:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_auto_20170103_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='channel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='messenger.Channel'),
        ),
    ]
