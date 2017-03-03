# Django Imports
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def test_api(request, api_version):
    response = JsonResponse(data={'success': True, 'api_version': api_version})
    return response
