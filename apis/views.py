# App Imports
import models

# Django Imports
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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
