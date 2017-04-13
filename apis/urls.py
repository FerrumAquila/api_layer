# App Imports
import views

# Django Imports
from django.conf.urls import url


urlpatterns = [
    # App APIs
    url(r'^v/(?P<api_version>[a-z A-Z 0-9]+)/(?P<api_name>[a-z A-Z 0-9 \/]+)/$', views.apis, name='apis'),
]
