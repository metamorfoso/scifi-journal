# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_auto_20160801_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='pub_date',
            field=models.DateField(blank=True, null=True, verbose_name='issue publication date'),
        ),
    ]
