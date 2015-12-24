# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 17:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20151223_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='recommender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
