# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-27 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0006_auto_20180917_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.CharField(blank=True, default='2018-09-27', max_length=100),
        ),
        migrations.AlterField(
            model_name='categories',
            name='date',
            field=models.CharField(blank=True, default='2018-09-27', max_length=100),
        ),
    ]