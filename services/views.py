# App Imports
import models
import serializer
import form_models
import calendar
import time

# Package Imports
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

# Django Imports
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

# CarCrew Django Imports
from collections import OrderedDict
from django.http import JsonResponse
from django.template.loader import render_to_string


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
class ListServiceAPIView(generics.ListAPIView):
    serializer_class = serializer.ServiceAPIDRF
    lookup_url_kwarg = 'service'

    def get_queryset(self):
        service = self.kwargs.get(self.lookup_url_kwarg)
        return models.ServiceAPI.objects.filter(service__name=service)


class CreateServiceAPIView(generics.CreateAPIView):
    serializer_class = serializer.ServiceAPIDRF
    lookup_url_kwarg = 'service'

    def get_queryset(self):
        service = self.kwargs.get(self.lookup_url_kwarg)
        return models.ServiceAPI.objects.filter(service__name=service)


class ServiceAPIOperationsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.ServiceAPIDRF
    authentication_classes = (TokenAuthentication, )
    queryset = models.ServiceAPI.objects.all()


# HTML Views
@login_required(login_url='/login/')
def register_service(request):
    form, form_id = form_models.CreateServiceForm(request).form_data
    return render_to_response('services/index.html', {'form': form, 'form_id': form_id})


@login_required(login_url='/login/')
def update_service(request, service):
    service = models.Service.objects.get(name=service)
    form, form_id = form_models.UpdateServiceForm(request, service).form_data
    service_api_forms = [service_api.update_form(request) for service_api in service.apis.all()]
    return render_to_response('services/index.html', {'service': service, 'form': form, 'form_id': form_id,
                                                      'service_api_forms': service_api_forms})


@login_required(login_url='/login/')
def register_service_api(request, service):
    service = models.Service.objects.get(name=service)
    form, form_id = form_models.CreateServiceAPIForm(request, service).form_data
    return render_to_response('services/api.html', {'form': form, 'form_id': form_id,
                                                    'timestamp': calendar.timegm(time.gmtime())})


properties = {
    'statuses': OrderedDict((
        ('pending', {
            'verbose': 'Pending',
            'color_class': 'bgm-gray',
            'items': 0,
        }),
        ('scheduled', {
            'verbose': 'Scheduled',
            'color_class': 'bgm-blue',
            'items': 0,
        }),
        ('picked', {
            'verbose': 'Picked',
            'color_class': 'bgm-yellow',
            'items': 0,
        }),
        ('delivered', {
            'verbose': 'Delivered',
            'color_class': 'bgm-green',
            'items': 0,
        }),
    )),
    'distribution_class': 'col-md-3',
    'status_slab_color_class': 'bgm-white',
}


def dashboard(request):
    delivery_notes = [{'id': 1, 'status': 'pending'}, {'id': 2, 'status': 'picked'}, {'id': 3, 'status': 'delivered'},
                      {'id': 4, 'status': 'picked'}, {'id': 5, 'status': 'scheduled'}, {'id': 6, 'status': 'delivered'},
                      {'id': 7, 'status': 'pending'}, {'id': 8, 'status': 'picked'}, {'id': 9, 'status': 'delivered'},
                      {'id': 10, 'status': 'picked'}, {'id': 11, 'status': 'scheduled'}]

    for delivery_note in delivery_notes:
        prop = properties['statuses'][delivery_note['status']]
        prop['items'] += 1

    return render_to_response('carcrew/delivery-note/dashboard.html',
                              {'properties': properties, 'delivery_notes': delivery_notes})


def delivery_details_html(request):
    import datetime
    now = datetime.datetime.now()
    pk = 'ajax_%s' % (now.today() - now).seconds
    delivery_note = {'id': pk, 'status': 'pending'}
    delivery_html = render_to_string('carcrew/delivery-note/delivery_note.html', {'properties': properties, 'note': delivery_note})
    response = {'success': True, 'html': delivery_html, 'id': pk}
    return JsonResponse(data=response)
