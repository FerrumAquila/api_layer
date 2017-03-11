# App Imports
import models
from services import models as service_models

# Django Imports
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def apis(request, api_name, api_version):
    sample_request = {
        'pageId': 'homepage',
        'pageType': 'homepage',
        'userType': 'every'
    }
    end_point = models.EndPoint.objects.get(name=api_name)
    response = JsonResponse(data=end_point.fetch_data(sample_request))
    return response
