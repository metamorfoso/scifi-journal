# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-14 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0020_auto_20170611_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='openForSubmissions',
            field=models.BooleanField(default=False),
        ),
    ]