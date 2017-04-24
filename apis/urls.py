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

    url(r'^update/(?P<api>[-\w]+)/$',
        views.update_api,
        name='api-update'),

    # EndPoints
    url(r'^(?P<api>[-\w]+)/endpoint/new/$',
        views.register_end_point,
        name='end-point-new'),

    ## DRF APIs
    # APIs
    url(r'^drf/create/$',
        views.CreateAPIView.as_view(),
        name='api-drf-create'),

    url(r'^drf/update/(?P<pk>[0-9]+)/$',
        views.APIOperationsView.as_view(),
        name='api-drf-update'),

    url(r'^drf/delete/(?P<pk>[0-9]+)/$',
        views.APIOperationsView.as_view(),
        name='api-drf-delete'),


    # EndPoints
    url(r'^(?P<api>[0-9]+)/api/drf/list/$',
        views.ListEndPointView.as_view(),
        name='end-point-drf-list'),

    url(r'^endpoint/drf/create/$',
        views.CreateEndPointView.as_view(),
        name='end-point-drf-create'),

    url(r'^endpoint/drf/update/(?P<pk>[0-9]+)/$',
        views.EndPointOperationsView.as_view(),
        name='end-point-drf-update'),

    url(r'^endpoint/drf/delete/(?P<pk>[0-9]+)/$',
        views.EndPointOperationsView.as_view(),
        name='end-point-drf-delete'),
]
