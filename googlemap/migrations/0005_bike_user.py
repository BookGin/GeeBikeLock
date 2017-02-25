# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 14:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('googlemap', '0004_user2bike'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='own_bike', to=settings.AUTH_USER_MODEL),
        ),
    ]
