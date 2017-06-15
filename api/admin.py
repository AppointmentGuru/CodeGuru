# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ICD10Code

class ICD10CodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'level', 'path', 'see')
    search_fields = ('code','title')

admin.site.register(ICD10Code, ICD10CodeAdmin)
