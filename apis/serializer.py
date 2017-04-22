# App Imports
import models

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

    class Meta:
        model = models.EndPoint

    def create(self, validated_data):
        return super(EndPointDRF, self).create(validated_data)

    def validate(self, attrs):
        return super(EndPointDRF, self).validate(attrs)

    def update(self, instance, validated_data):
        return super(EndPointDRF, self).update(instance, validated_data)
