# App Imports
from api_layer.custom_model_class import AetosModel

# Django Imports
from django.db import models


class Service(AetosModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name
