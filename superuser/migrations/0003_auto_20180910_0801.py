# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0002_auto_20180829_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.CharField(blank=True, default='2018-09-10', max_length=100),
        ),
        migrations.AlterField(
            model_name='categories',
            name='date',
            field=models.CharField(blank=True, default='2018-09-10', max_length=100),
        ),
    ]
