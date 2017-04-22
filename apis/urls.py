# App Imports
import views

# Django Imports
from django.conf.urls import url


urlpatterns = [
    # App APIs
    url(r'^v/(?P<api_version>[a-z A-Z 0-9]+)/(?P<api_name>[a-z A-Z 0-9 \/]+)/$', views.apis, name='apis'),

    ## Dashboard HTMLs
    # APIs
    url(r'^new/$',
        views.register_api,
        name='api-new'),

    # EndPoints
    url(r'^(?P<api>[-\w]+)/endpoint/new/$',
        views.register_end_point,
        name='end-point-new'),

    ## DRF APIs
    # APIs
    url(r'^drf/create/$',
        views.CreateAPIView.as_view(),
        name='api-drf-create'),


    # EndPoints
    url(r'^endpoint/drf/create/$',
        views.CreateEndPointView.as_view(),
        name='end-point-drf-create'),
]
