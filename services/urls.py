# App Imports
import views

# Django Imports
from django.conf.urls import url


urlpatterns = [
    # CREATE HTMLs
    url(r'^new/$', views.register_service, name='service-register-new'),
    url(r'^(?P<service>[-\w]+)/api/new/$', views.register_api, name='service-api-register-new'),

    # DRF APIs
    url(r'^drf/create/$', views.CreateServiceView.as_view(), name='service-drf-create'),
    url(r'^api/drf/create/$', views.CreateServiceAPIView.as_view(), name='service-api-drf-create'),
]
