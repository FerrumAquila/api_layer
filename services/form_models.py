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
    def __init__(self, request, service):
        super(CreateServiceAPIForm, self).__init__(request, reverse('service-api-drf-create', kwargs={'service_id': service.pk}), parent=service)
        self.display_fields.pop(self.display_fields.index('service'))


class UpdateServiceForm(ServiceForm):
    def __init__(self, request, service):
        super(UpdateServiceForm, self).__init__(request, reverse('service-drf-update', kwargs={'pk': service.pk}),
                                                instance=service)


class UpdateServiceAPIForm(ServiceAPIForm):
    def __init__(self, request, service_api):
        super(UpdateServiceAPIForm, self).__init__(request, reverse('service-api-drf-update', kwargs={'pk': service_api.pk}), instance=service_api, parent=service_api.service)
        self.display_fields.pop(self.display_fields.index('service'))

