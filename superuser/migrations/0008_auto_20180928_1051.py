# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0007_auto_20180927_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.CharField(blank=True, max_length=100, default='2018-09-28'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='date',
            field=models.CharField(blank=True, max_length=100, default='2018-09-28'),
        ),
    ]
