# App Imports
import utils
import form_models
from api_layer.custom_model_class import AetosModel

# Packaged Imports
import json
import requests
from aetos_serialiser.serialisers import Serializer, VersionedSerializer
from aetos_serialiser.helpers import dict_reducer

# Django Imports
from django.db import models
from django.template.loader import render_to_string


class Service(AetosModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    base_url = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name


class ServiceAPI(AetosModel):
    service = models.ForeignKey(Service, related_name='apis')
    body_map = models.TextField(default='{}')
    endpoint = models.CharField(max_length=255)
    doc_yaml = models.TextField(default='')

    @staticmethod
    def _parse_key_info(key_info):
        return tuple([key_info[0], eval(key_info[1])])

    @property
    def serialiser(self, versioned=False):
        body_map = {required_key: self._parse_key_info(key_info)
                    for required_key, key_info in json.loads(self.body_map).items()}

        class APISerialiser(Serializer):
            BODY_MAP = body_map
            REDUCER = dict_reducer

        class VersionedAPISerialiser(VersionedSerializer):
            BODY_MAP = body_map
            REDUCER = dict_reducer

        return VersionedAPISerialiser if versioned else APISerialiser

    def fetch_data(self, params_data):
        url = self.service.base_url + self.endpoint
        params = {param['name']: params_data[param['name']] for param in self.api_data['parameters']}
        response = requests.request(self.api_data['action'], url=url, params=params)
        return response.json()

    @property
    def api_data(self):
        return utils.YAMLParser(self.doc_yaml).instance

    def update_form(self, request):
        form, form_id = form_models.UpdateServiceAPIForm(request, self).form_data
        return render_to_string('services/api.html', {'object': self, 'form': form, 'form_id': form_id, 'timestamp': self.id})
