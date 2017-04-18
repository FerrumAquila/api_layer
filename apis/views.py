# App Imports
import models

# Django Imports
from django.http import JsonResponse
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
