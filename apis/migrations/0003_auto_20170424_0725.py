# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-24 07:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_endpoint_doc_yaml'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='api',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='api',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='endpoint',
            name='modified_by',
        ),
    ]
