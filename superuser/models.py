# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime
from django.db import models
# Create your models here.


class categories(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, max_length=250)
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    date = models.CharField(max_length=100, default=datetime.today().strftime('%Y-%m-%d'), blank=True)
    class Meta:
        db_table = "categories"



class blog(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, max_length=250)
    categories_id = models.ForeignKey(categories, blank=True, null=True, max_length=250)
    title = models.CharField(max_length=2000,null=True,blank=True)
    slug = models.SlugField(max_length=2000,null=True,blank=True)
    image = models.ImageField(upload_to='picfolder',null=True,blank=True)
    # categories = models.CharField(max_length=2000,null=True,blank=True)
    description = models.CharField(max_length=50000,null=True,blank=True)
    meta_title = models.CharField(max_length=2000,null=True,blank=True)
    meta_keyword = models.CharField(max_length=2000,null=True,blank=True)
    meta_description = models.CharField(max_length=2000,null=True,blank=True)
    date = models.CharField(max_length=100, default=datetime.today().strftime('%Y-%m-%d'), blank=True)
    def save(self):
        super(blog, self).save()
        self.slug = '%s' % (
            slugify(self.title)
        )
        super(blog, self).save()
    class Meta:
        db_table = "blog"
    def __str__(self):
        return self.title


