# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

"""
Chapter -> Section -> Code -> Code -> ...
"""
class Chapter(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class Section(models.Model):
    parent = models.ForeignKey('Chapter', blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class Code(models.Model):
    section = models.ForeignKey('Section', blank=True, null=True)
    parent = models.ForeignKey('Code', blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    includes = ArrayField(models.TextField(), blank=True, null=True, help_text='The word \'Includes\' appears immediately under certain categories to further define, or give examples of, the content of the category.')
    excludes1 = ArrayField(models.TextField(), blank=True, null=True, help_text='A type 1 Excludes note is a pure excludes.  It means \'NOT CODED HERE!\'  An Excludes1 note indicates that the code excluded should never be used at the same time as the code above the Excludes1 note.  An Excludes1 is used when two conditions cannot occur together, such as a congenital form versus an acquired form of the same condition.')
    excludes2 = ArrayField(models.TextField(), blank=True, null=True, help_text='A type 2 excludes note represents \'Not included here\'.  An excludes2 note indicates that the condition excluded is not part of the condition it is excluded from but a patient may have both conditions at the same time.  When an Excludes2 note appears under a code it is acceptable to use both the code and the excluded code together.')
    inclusion_term = ArrayField(models.TextField(), blank=True, null=True, help_text='Certain conditions have both an underlying etiology and multiple body system manifestations due to the underlying etiology.  For such conditions the ICD-10-CM has a coding convention that requires the underlying condition be sequenced first followed by the manifestation.  Wherever such a combination exists there is a \'use additional code\' note at the etiology code, and a \'code first\' note at the manifestation code.  These instructional notes indicate the proper sequencing order of the codes, etiology followed by manifestation. In most cases the manifestation codes will have in the code title, \'in diseases classified elsewhere.\'  Codes with this title are a component of the etiology/ manifestation convention. The code title indicates that it is a manifestation code.  \'In diseases classified elsewhere\' codes are never permitted to be used as first listed or principal diagnosis codes. They must be used in conjunction with an underlying condition code and they must be listed following the underlying condition.')
    use_additional_code = ArrayField(models.TextField(), blank=True, null=True, help_text='A code also note instructs that 2 codes may be required to fully describe a condition but the sequencing of the two codes is discretionary, depending on the severity of the conditions and the reason for the encounter.')

class ICD10Code(models.Model):

    def __str__(self):
        return '{}: {}'.format(self.code, self.title)

    parent = models.ForeignKey('ICD10Code', blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    see = models.CharField(max_length=250, blank=True, null=True)
    level = models.PositiveIntegerField(blank=True, null=True)
    raw = models.TextField(default='{}')

    @property
    def path(self):
        code_path = []
        code = self
        while code.parent:
            if code.title is not None:
                part = '[{}] {}'.format(code.code, code.title)
                code_path.append(part)
            code = code.parent
        code_path.reverse()
        return (" > ").join(code_path)
