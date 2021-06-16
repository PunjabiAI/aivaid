# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0003_auto_20180910_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.CharField(max_length=100, default='2018-09-14', blank=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='date',
            field=models.CharField(max_length=100, default='2018-09-14', blank=True),
        ),
    ]
