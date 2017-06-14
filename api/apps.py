# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
import algoliasearch_django as algoliasearch

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        ICD10Code = self.get_model('ICD10Code')
        import pdb;pdb.set_trace()
        algoliasearch.register(ICD10Code)