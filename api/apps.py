# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex

class ICD10CodeIndex(AlgoliaIndex):
    fields = ('code', 'path', 'level', 'see')

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        ICD10Code = self.get_model('ICD10Code')
        algoliasearch.register(ICD10Code, ICD10CodeIndex)
