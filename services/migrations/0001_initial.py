# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-03 12:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_active', models.BooleanField(default=False)),
                ('meta', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_services', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_services', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
