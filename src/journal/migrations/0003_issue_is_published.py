# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_story_author_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
