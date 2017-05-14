# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-05-14 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0009_auto_20170428_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.ImageField(blank=True, upload_to='cover_image_uploads/')),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('artist_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='issue',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='cover',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Issue'),
        ),
    ]
