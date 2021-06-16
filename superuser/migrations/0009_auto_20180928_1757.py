# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0008_auto_20180928_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='categories',
            field=models.CharField(max_length=2000, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(max_length=50000, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='picfolder', null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='meta_description',
            field=models.CharField(max_length=2000, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='meta_keyword',
            field=models.CharField(max_length=2000, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='meta_title',
            field=models.CharField(max_length=2000, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=2000, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=2000, blank=True, null=True),
        ),
    ]
