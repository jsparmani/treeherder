# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-18 08:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0005_use_matcher_name_for_unique_constraint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='failurematch',
            name='matcher',
        ),
        migrations.RemoveField(
            model_name='textlogerrormatch',
            name='matcher',
        ),
    ]