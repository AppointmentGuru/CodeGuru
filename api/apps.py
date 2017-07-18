# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex

class CodeIndex(AlgoliaIndex):
    fields = ('name', 'description')

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        Code = self.get_model('Code')
        # algoliasearch.register(Code, CodeIndex)
