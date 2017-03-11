# App Imports
import views

# Django Imports
from django.conf.urls import url


urlpatterns = [
    ## HTMLs
    # Services
    url(r'^new/$',
        views.register_service,
        name='service-register-new'),

    url(r'^update/(?P<service>[-\w]+)/$',
        views.update_service,
        name='service-update'),

    # Service APIs

    url(r'^(?P<service>[-\w]+)/api/new/$',
        views.register_api,
        name='service-api-register-new'),


    ## DRF APIs
    # Services
    url(r'^drf/create/$',
        views.CreateServiceView.as_view(),
        name='service-drf-create'),

    url(r'^drf/update/(?P<pk>[0-9]+)/$',
        views.ServiceOperationsView.as_view(),
        name='service-drf-update'),

    # Service APIs
    url(r'^(?P<service_id>[0-9]+)/api/drf/create/$',
        views.CreateServiceAPIView.as_view(),
        name='service-api-drf-create'),

    url(r'^(?P<service_id>[0-9]+)/api/drf/update/(?P<pk>[0-9]+)/$',
        views.ServiceAPIOperationsView.as_view(),
        name='service-api-drf-update'),
]
