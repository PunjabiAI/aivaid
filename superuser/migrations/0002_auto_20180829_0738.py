# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-29 07:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='meta_keyword',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='meta_title',
        ),
    ]