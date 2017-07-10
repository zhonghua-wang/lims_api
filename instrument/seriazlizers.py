from rest_framework import serializers
from . import models


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        exclude = []


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufacturer
        exclude = []


class ReservationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReservationType
        exclude = []


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instrument
        exclude = []
        admin = serializers.Field(source='User.last_name')


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        exclude = []
