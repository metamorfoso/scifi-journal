# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-05-14 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0010_auto_20170514_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]