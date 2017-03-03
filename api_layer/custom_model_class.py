# Package Imports
from model_utils.models import TimeStampedModel

# Django Imports
from django.db import models
from django.conf import settings


class AetosModel(TimeStampedModel):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_%(class)ss')
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='modified_%(class)ss')
    is_active = models.BooleanField(default=False)
    meta = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True
