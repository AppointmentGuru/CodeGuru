# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ICD10Code(models.Model):

    def __str__(self):
        return '{}: {}'.format(self.code, self.title)

    parent = models.ForeignKey('ICD10Code', blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    see = models.CharField(max_length=250, blank=True, null=True)
    raw = models.TextField(default='{}')

