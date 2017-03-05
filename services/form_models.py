# App Imports
import models
from aetos_material import html_forms

# Django Imports
from django.core.urlresolvers import reverse


class ServiceForm(html_forms.MaterialForm):
    DISPLAY_MAP = {
        'name': {'group_name': 'Info', 'pos': 1, 'col_class': 'col-sm-6'},
        'description': {'group_name': 'Info', 'pos': 2, 'col_class': 'col-sm-6'},
    }

    def __init__(self, request, action, instance=None):
        super(ServiceForm, self).__init__(request, models.Service, action, instance=instance)


class CreateServiceForm(ServiceForm):
    def __init__(self, request):
        super(CreateServiceForm, self).__init__(request, reverse('service-drf-create'))
