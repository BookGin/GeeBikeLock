# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 13:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('googlemap', '0003_auto_20170225_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='User2bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike_id', models.CharField(max_length=256)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bike', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
