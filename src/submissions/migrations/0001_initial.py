# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.FileField(upload_to='submission_uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Submitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='submission',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submissions.Submitter'),
        ),
    ]