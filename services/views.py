# App Imports
import models
import serializer
import form_models

# Package Imports
from rest_framework import generics

# Django Imports
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


class CreateServiceView(generics.ListCreateAPIView):
    serializer_class = serializer.ServiceDRF
    queryset = models.Service.objects.all()


class CreateServiceAPIView(generics.ListCreateAPIView):
    serializer_class = serializer.ServiceAPIDRF
    lookup_url_kwarg = 'service'

    def get_queryset(self):
        service = self.kwargs.get(self.lookup_url_kwarg)
        return models.ServiceAPI.objects.filter(service__name=service)


@login_required(login_url='/login/')
def register_service(request):
    form = form_models.CreateServiceForm(request).form
    return render_to_response('services/index.html', {'form': form})


@login_required(login_url='/login/')
def register_api(request):
    form = form_models.CreateServiceAPIForm(request).form
    return render_to_response('services/api.html', {'form': form})
