# App Imports
import models
import serializer
import form_models

# Package Imports
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

# Django Imports
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


# Service DRF Views
class ServicesListDashboard(ListView):
    model = models.Service
    paginate_by = 15
    template_name = 'services/dashboard.html'

    def get_queryset(self):
        return models.Service.objects.all()


class CreateServiceView(generics.ListCreateAPIView):
    serializer_class = serializer.ServiceDRF
    queryset = models.Service.objects.all()


class ServiceOperationsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.ServiceDRF
    authentication_classes = (TokenAuthentication, )
    queryset = models.Service.objects.all()


# Service API DRF Views
class CreateServiceAPIView(generics.ListCreateAPIView):
    serializer_class = serializer.ServiceAPIDRF
    lookup_url_kwarg = 'service'

    def get_queryset(self):
        service = self.kwargs.get(self.lookup_url_kwarg)
        return models.ServiceAPI.objects.filter(service__name=service)


class ServiceAPIOperationsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.ServiceAPIDRF
    authentication_classes = (TokenAuthentication, )
    lookup_url_kwarg = 'service_id'

    def get_queryset(self):
        service = self.kwargs.get(self.lookup_url_kwarg)
        return models.ServiceAPI.objects.filter(service__name=service)


# HTML Views
@login_required(login_url='/login/')
def register_service(request):
    form, form_id = form_models.CreateServiceForm(request).form_data
    return render_to_response('services/index.html', {'form': form, 'form_id': form_id})


@login_required(login_url='/login/')
def update_service(request, service):
    service = models.Service.objects.get(name=service)
    form, form_id = form_models.UpdateServiceForm(request, service).form_data
    return render_to_response('services/index.html', {'service': service, 'form': form, 'form_id': form_id})


@login_required(login_url='/login/')
def register_api(request, service):
    service = models.Service.objects.get(name=service)
    form, form_id = form_models.CreateServiceAPIForm(request, service).form_data
    return render_to_response('services/api.html', {'form': form, 'form_id': form_id})
