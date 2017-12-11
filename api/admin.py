# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ICD10Code, Code, ProcessCode

class ICD10CodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'level', 'path', 'see')
    search_fields = ('code','title')

class CodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'includes', 'excludes1', 'excludes2', 'inclusion_term', 'use_additional_code',)
    search_fields = ('name',)

class ProcessCodeAdmin(admin.ModelAdmin):
    list_display = ('practice_type_code', 'name', 'description', 'discovery_rate',)
    search_fields = ('name','practice_type_code',)
    filter_fields = ('practice_type_code',)

admin.site.register(Code, CodeAdmin)
admin.site.register(ProcessCode, ProcessCodeAdmin)
