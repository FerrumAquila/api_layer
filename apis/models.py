# App Imports
from api_layer import utils
from api_layer.custom_model_class import AetosModel
from services import models as service_models

# Packaged Imports
import json
from aetos_serialiser.serialisers import Serializer, VersionedSerializer
from aetos_serialiser.helpers import dict_reducer

# Django Imports
from django.db import models


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

    @staticmethod
    def _parse_key_info(key_info):
        return tuple([key_info[0], eval(key_info[1])])

    def fetch_data(self, params_data):
        api_data = dict()
        for service_api in self.service_apis.all():
            api_params = self._request_serialiser(params_data).required_json
            api_data.update({'root_data': {service_api.pk: service_api.fetch_data(api_params)}})
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
        super(EndPoint, self).save(*args, **kwargs)