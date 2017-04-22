# App Imports
import form_models
from api_layer import utils
from api_layer.custom_model_class import AetosModel
from services import models as service_models

# Packaged Imports
import json
from aetos_serialiser.serialisers import Serializer, VersionedSerializer
from aetos_serialiser.helpers import dict_reducer

# Django Imports
from django.db import models
from django.template.loader import render_to_string


class API(AetosModel):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=63)


class EndPoint(AetosModel):
    api = models.ForeignKey(API, related_name='endpoints')
    request_map = models.TextField(default='{}')
    response_map = models.TextField(default='{}')
    name = models.CharField(max_length=255)
    service_apis = models.ManyToManyField(service_models.ServiceAPI, related_name='endpoints')
    doc_yaml = models.TextField(default='')

    @property
    def api_data(self):
        return utils.YAMLParser(self.doc_yaml).instance

    @property
    def get_request_map(self):
        type_map = {'integer': 'int', 'object': 'dict', 'string': 'str'}
        params = self.api_data['parameters']
        return {param['key']: [param['name'], type_map[param['type']]] for param in params}

    @property
    def get_response_map(self):
        type_map = {'integer': 'int', 'object': 'dict', 'string': 'str'}
        params = self.api_data['responses'][200]['schema']['properties']
        return {param_key: [param_value['key'], type_map[param_value['type']]] for param_key, param_value in params.items()}

    @staticmethod
    def _parse_key_info(key_info):
        return tuple([key_info[0], eval(key_info[1])])

    def fetch_data(self, params_data):
        api_data = dict()
        for service_api in self.service_apis.all():
            api_params = self._request_serialiser(params_data).required_json
            api_data.update({'root_data': {str(service_api.pk): service_api.fetch_data(api_params)}})
        return self._response_serialiser(api_data).required_json

    @property
    def _request_serialiser(self, versioned=False):
        return self._serialiser('request', versioned)

    @property
    def _response_serialiser(self, versioned=False):
        return self._serialiser('response', versioned)

    def _serialiser(self, sr_type, versioned=False):
        map_dict = getattr(self, '%s_map' % sr_type) if sr_type in ['request', 'response'] else None
        if map_dict:
            body_map = {required_key: self._parse_key_info(key_info)
                        for required_key, key_info in json.loads(map_dict).items()}
        else:
            raise Exception('Only Request and Response Body Maps Available')

        class APISerialiser(Serializer):
            BODY_MAP = body_map
            REDUCER = dict_reducer

        class VersionedAPISerialiser(VersionedSerializer):
            BODY_MAP = body_map
            REDUCER = dict_reducer

        return VersionedAPISerialiser if versioned else APISerialiser

    def save(self, *args, **kwargs):
        self.request_map = json.dumps(self.get_request_map)
        self.response_map = json.dumps(self.get_response_map)
        super(EndPoint, self).save(*args, **kwargs)

    def update_form(self, request):
        form, form_id = form_models.UpdateEndPointForm(request, self).form_data
        return render_to_string('services/api.html', {'object': self, 'form': form, 'form_id': form_id, 'timestamp': self.id})
