# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-05-14 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0011_author_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]