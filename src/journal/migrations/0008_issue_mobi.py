# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-30 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0007_auto_20161010_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='mobi',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='issue as Mobi document'),
        ),
    ]