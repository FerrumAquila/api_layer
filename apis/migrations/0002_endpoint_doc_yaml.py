# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-18 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoint',
            name='doc_yaml',
            field=models.TextField(default=b''),
        ),
    ]
