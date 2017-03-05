# App Imports
import models
import serializer

# Package Imports
from rest_framework import generics


class CreateServiceView(generics.ListCreateAPIView):
    serializer_class = serializer.ServiceDRF
    queryset = models.Service.objects.all()


class CreateServiceAPIView(generics.ListCreateAPIView):
    serializer_class = serializer.ServiceAPIDRF
    queryset = models.ServiceAPI.objects.all()
