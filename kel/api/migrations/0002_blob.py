# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('content_type', models.CharField(default='application/octet-stream', max_length=150)),
            ],
        ),
    ]
