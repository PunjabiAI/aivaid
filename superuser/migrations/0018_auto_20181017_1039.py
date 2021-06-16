# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-17 05:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('superuser', '0017_auto_20181017_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='categories_id',
            field=models.ForeignKey(blank=True, max_length=250, null=True, on_delete=django.db.models.deletion.CASCADE, to='superuser.categories'),
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(blank=True, max_length=250, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]