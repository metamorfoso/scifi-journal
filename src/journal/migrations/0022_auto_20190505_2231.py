# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-05-05 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0021_issue_openforsubmissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='bandcamp_album_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
