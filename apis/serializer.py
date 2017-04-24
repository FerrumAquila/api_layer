# App Imports
import models
from services import models as service_models

# Package Imports
from rest_framework import serializers


class APIDRF(serializers.ModelSerializer):

    class Meta:
        model = models.API

    def create(self, validated_data):
        return super(APIDRF, self).create(validated_data)

    def validate(self, attrs):
        return super(APIDRF, self).validate(attrs)

    def update(self, instance, validated_data):
        return super(APIDRF, self).update(instance, validated_data)


class EndPointDRF(serializers.ModelSerializer):
    service_apis = serializers.PrimaryKeyRelatedField(many=True, queryset=service_models.ServiceAPI.objects.all())

    class Meta:
        model = models.EndPoint
        fields = ('pk', 'api', 'request_map', 'response_map', 'name', 'service_apis', 'doc_yaml')

    def create(self, validated_data):
        service_apis = validated_data.pop('service_apis')
        super_response = super(EndPointDRF, self).create(validated_data)
        for service_api in service_apis:
            super_response.service_apis.add(service_api)
        return super_response

    def validate(self, attrs):
        return super(EndPointDRF, self).validate(attrs)

    def update(self, instance, validated_data):
        service_apis = validated_data.pop('service_apis')
        instance.service_apis.clear()
        for service_api in service_apis:
            instance.service_apis.add(service_api)
        return super(EndPointDRF, self).update(instance, validated_data)
