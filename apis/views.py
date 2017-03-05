# App Imports
from services import models as service_models

# Django Imports
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def test_api(request, api_version):
    data = service_models.ServiceAPI.objects.all().latest('id').serialiser(
        {'data': {'success': True, 'api_version': api_version}}).required_json
    response = JsonResponse(data=data)
    return response
