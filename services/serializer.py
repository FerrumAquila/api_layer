# App Imports
import models

# Package Imports
from rest_framework import serializers


class ServiceDRF(serializers.ModelSerializer):

    class Meta:
        model = models.Service

    def create(self, validated_data):
        print validated_data
        return super(ServiceDRF, self).create(validated_data)

    def validate(self, attrs):
        return super(ServiceDRF, self).validate(attrs)

    def update(self, instance, validated_data):
        print validated_data
        return super(ServiceDRF, self).update(instance, validated_data)


class ServiceAPIDRF(serializers.ModelSerializer):

    class Meta:
        model = models.ServiceAPI

    def create(self, validated_data):
        return super(ServiceAPIDRF, self).create(validated_data)

    def validate(self, attrs):
        return super(ServiceAPIDRF, self).validate(attrs)

    def update(self, instance, validated_data):
        return super(ServiceAPIDRF, self).update(instance, validated_data)
