__author__ = 'ironeagle'

from django.conf.urls import url

import views as app_views
import docs as app_docs

urlpatterns = [
    url(r'^home/$', app_views.home, name='core-home'),
    url(r'^dashboard/$', app_views.dashboard, name='core-dashboard'),
    url(r'^login/$', app_views.sign_in, name='core-sign-in'),
    url(r'^logout/$', app_views.sign_out, name='core-sign-out'),
    url(r'^$', app_views.home, name='core-home'),
] + app_docs.urlpatterns
