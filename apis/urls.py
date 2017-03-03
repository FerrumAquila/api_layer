# App Imports
import views

# Django Imports
from django.conf.urls import url


urlpatterns = [
    # App APIs
    url(r'^test$', views.test_api, name='apis-test'),
]
