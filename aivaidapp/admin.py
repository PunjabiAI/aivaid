# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from aivaidapp.form import questions_form
from aivaidapp.models import disease_db, questions_db, symptoms_db, symptoms_type

# Register your models here.

admin.site.register(symptoms_type)
admin.site.register(symptoms_db)
admin.site.register(disease_db)
admin.site.register(questions_db)

