# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20151223_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
