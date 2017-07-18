# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ICD10Code, Code

class ICD10CodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'level', 'path', 'see')
    search_fields = ('code','title')

class CodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'includes', 'excludes1', 'excludes2', 'inclusion_term', 'use_additional_code',)
    search_fields = ('name',)

admin.site.register(Code, CodeAdmin)
