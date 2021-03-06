# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-06-02 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0003_submission_guidelines_submissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='contents',
            field=models.TextField(blank=True, max_length=30000),
        ),
        migrations.AlterField(
            model_name='submission_guidelines',
            name='contact',
            field=models.TextField(blank=True, max_length=30000),
        ),
        migrations.AlterField(
            model_name='submission_guidelines',
            name='content',
            field=models.TextField(blank=True, max_length=30000),
        ),
        migrations.AlterField(
            model_name='submission_guidelines',
            name='formatting',
            field=models.TextField(blank=True, max_length=30000),
        ),
        migrations.AlterField(
            model_name='submission_guidelines',
            name='general',
            field=models.TextField(blank=True, max_length=30000),
        ),
        migrations.AlterField(
            model_name='submission_guidelines',
            name='submissions',
            field=models.TextField(blank=True, max_length=30000),
        ),
    ]
