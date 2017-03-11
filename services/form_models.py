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


class ServiceAPIForm(html_forms.MaterialForm):
    DISPLAY_MAP = {
        'name': {'group_name': 'Info', 'pos': 1, 'col_class': 'col-sm-6'},
        'description': {'group_name': 'Info', 'pos': 2, 'col_class': 'col-sm-6'},
    }

    def __init__(self, request, action, instance=None, parent=None):
        super(ServiceAPIForm, self).__init__(request, models.ServiceAPI, action, instance=instance, parent=parent)


class CreateServiceForm(ServiceForm):
    def __init__(self, request):
        super(CreateServiceForm, self).__init__(request, reverse('service-drf-create'))


class CreateServiceAPIForm(ServiceAPIForm):
    def __init__(self, request, parent):
        super(CreateServiceAPIForm, self).__init__(request, reverse('service-api-drf-create'), parent=parent)
        self.display_fields.pop(self.display_fields.index('service'))


class UpdateServiceForm(ServiceForm):
    def __init__(self, request, instance):
        super(UpdateServiceForm, self).__init__(request, reverse('service-drf-update'), instance=instance)


class UpdateServiceAPIForm(ServiceAPIForm):
    def __init__(self, request, parent, instance):
        super(UpdateServiceAPIForm, self).__init__(request, reverse('service-api-drf-update'), instance=instance, parent=parent)
        self.display_fields.pop(self.display_fields.index('service'))

