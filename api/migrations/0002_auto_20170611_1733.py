# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icd10code',
            name='code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='icd10code',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
