from rest_framework import serializers
from . import models
from core.serializer import UserSerializer


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


class ChargeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChargeType
        exclude = []


class InstrumentSerializer(serializers.ModelSerializer):
    admin = UserSerializer()
    manufacturer = ManufacturerSerializer()
    department = DepartmentSerializer()
    charge_type = ChargeTypeSerializer()
    reservation_type = ReservationTypeSerializer()

    class Meta:
        model = models.Instrument
        exclude = []


class ReservationSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Reservation
        exclude = []


class ChargeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChargeType
        exclude = []
