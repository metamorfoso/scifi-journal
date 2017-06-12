# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-06-11 19:37
from __future__ import unicode_literals

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission_guidelines',
            name='contents',
        ),
        migrations.AddField(
            model_name='submission_guidelines',
            name='contact',
            field=froala_editor.fields.FroalaField(blank=True),
        ),
        migrations.AddField(
            model_name='submission_guidelines',
            name='content',
            field=froala_editor.fields.FroalaField(blank=True),
        ),
        migrations.AddField(
            model_name='submission_guidelines',
            name='formatting',
            field=froala_editor.fields.FroalaField(blank=True),
        ),
        migrations.AddField(
            model_name='submission_guidelines',
            name='general',
            field=froala_editor.fields.FroalaField(blank=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='contents',
            field=froala_editor.fields.FroalaField(blank=True),
        ),
    ]