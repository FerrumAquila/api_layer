# App Imports
import models
from aetos_material import html_forms

# Django Imports
from django.core.urlresolvers import reverse


class APIForm(html_forms.MaterialForm):
    DISPLAY_MAP = {
        'name': {'group_name': 'Info', 'pos': 1, 'col_class': 'col-sm-6'},
        'version': {'group_name': 'Info', 'pos': 2, 'col_class': 'col-sm-6'},
    }

    def __init__(self, request, action, instance=None):
        super(APIForm, self).__init__(request, models.API, action, instance=instance)


class EndPointForm(html_forms.MaterialForm):
    DISPLAY_MAP = {
        'name': {'group_name': 'Info', 'pos': 1, 'col_class': 'col-sm-6'},
        'doc_yaml': {'group_name': 'Doc', 'pos': 1, 'col_class': 'col-sm-12'},
    }

    def __init__(self, request, action, instance=None, parent=None):
        super(EndPointForm, self).__init__(request, models.EndPoint, action, instance=instance, parent=parent)


class CreateAPIForm(APIForm):
    def __init__(self, request):
        super(CreateAPIForm, self).__init__(request, reverse('api-drf-create'))


class CreateEndPointForm(EndPointForm):
    def __init__(self, request, api):
        super(CreateEndPointForm, self).__init__(request, reverse('end-point-drf-create'), parent=api)
        self.display_fields.pop(self.display_fields.index('api'))
        self.display_fields.pop(self.display_fields.index('response_map'))
        self.display_fields.pop(self.display_fields.index('request_map'))


class UpdateAPIForm(APIForm):
    def __init__(self, request, api):
        super(UpdateAPIForm, self).__init__(request, reverse('api-drf-update', kwargs={'pk': api.pk}), instance=api)


class UpdateEndPointForm(EndPointForm):
    def __init__(self, request, end_point):
        super(UpdateEndPointForm, self).__init__(request, reverse('end-point-drf-update', kwargs={'pk': end_point.pk}),
                                                 instance=end_point, parent=end_point.api)
        self.display_fields.pop(self.display_fields.index('api'))

