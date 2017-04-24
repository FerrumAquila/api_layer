# App Imports
import time
import models
import calendar
import serializer
import form_models

# Package Imports
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

# Django Imports
from django.http import JsonResponse
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


@csrf_exempt
def apis(request, api_version, api_name):
    sample_request = {
        'name': 'homepage',
        'type': 'homepage',
        'user': 'every'
    }
    end_point = models.EndPoint.objects.get(name=api_name)
    response = JsonResponse(data=end_point.fetch_data(sample_request))
    return response


# HTML Views
class APIListDashboard(ListView):
    model = models.API
    paginate_by = 15
    template_name = 'apis/dashboard.html'

    def get_queryset(self):
        return models.API.objects.all()

@login_required(login_url='/login/')
def register_api(request):
    form, form_id = form_models.CreateAPIForm(request).form_data
    return render_to_response('apis/index.html', {'form': form, 'form_id': form_id})


@login_required(login_url='/login/')
def update_api(request, api):
    api = models.API.objects.get(name=api)
    form, form_id = form_models.UpdateAPIForm(request, api).form_data
    end_point_forms = [end_point.update_form(request) for end_point in api.endpoints.all()]
    return render_to_response('apis/index.html', {'api': api, 'form': form, 'form_id': form_id,
                                                  'end_point_forms': end_point_forms})


@login_required(login_url='/login/')
def register_end_point(request, api):
    api = models.API.objects.get(name=api)
    form, form_id = form_models.CreateEndPointForm(request, api).form_data
    return render_to_response('apis/api.html', {'form': form, 'form_id': form_id,
                                                'timestamp': calendar.timegm(time.gmtime())})


# API DRF Views
class CreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializer.APIDRF
    queryset = models.API.objects.all()


class APIOperationsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.APIDRF
    authentication_classes = (TokenAuthentication, )
    queryset = models.API.objects.all()


# End Point DRF Views
class ListEndPointView(generics.ListAPIView):
    serializer_class = serializer.EndPointDRF
    lookup_url_kwarg = 'api'

    def get_queryset(self):
        api = self.kwargs.get(self.lookup_url_kwarg)
        return models.EndPoint.objects.filter(api__name=api)


class CreateEndPointView(generics.CreateAPIView):
    serializer_class = serializer.EndPointDRF
    lookup_url_kwarg = 'api'

    def get_queryset(self):
        api = self.kwargs.get(self.lookup_url_kwarg)
        return models.EndPoint.objects.filter(api__name=api)


class EndPointOperationsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.EndPointDRF
    authentication_classes = (TokenAuthentication, )
    queryset = models.EndPoint.objects.all()



