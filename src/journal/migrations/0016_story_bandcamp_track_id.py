# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-27 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0015_auto_20170527_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='bandcamp_track_id',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]