# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-11 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0013_auto_20181010_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.CharField(blank=True, default='2018-10-11', max_length=100),
        ),
        migrations.AlterField(
            model_name='categories',
            name='date',
            field=models.CharField(blank=True, default='2018-10-11', max_length=100),
        ),
    ]