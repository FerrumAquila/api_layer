# App Imports
import views

# Django Imports
from django.conf.urls import url


urlpatterns = [
    # DRF APIs
    url(r'^drf/create/$', views.CreateServiceView.as_view(), name='service-drf-create'),
]
