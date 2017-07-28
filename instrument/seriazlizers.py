from rest_framework import serializers
from . import models
from core.serializer import UserSerializer
from rest_framework_serializer_extensions.fields import HashIdField
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin


class DepartmentSerializer(SerializerExtensionsMixin, serializers.ModelSerializer):
    #id = HashIdField(model=models.Department)

    class Meta:
        model = models.Department
        exclude = []


class ManufacturerSerializer(serializers.ModelSerializer):
    id = HashIdField(model=models.Manufacturer)

    class Meta:
        model = models.Manufacturer
        exclude = []


class ReservationTypeSerializer(serializers.ModelSerializer):
    id = HashIdField(model=models.ReservationType)

    class Meta:
        model = models.ReservationType
        exclude = []


class ChargeTypeSerializer(serializers.ModelSerializer):
    id = HashIdField(model=models.ChargeType)

    class Meta:
        model = models.ChargeType
        exclude = []


class InstrumentSerializer(serializers.ModelSerializer):
    id = HashIdField(model=models.Instrument)

    admin = UserSerializer()
    manufacturer = ManufacturerSerializer()
    department = DepartmentSerializer()
    charge_type = ChargeTypeSerializer()
    reservation_type = ReservationTypeSerializer()

    class Meta:
        model = models.Instrument
        exclude = []


class ReservationSerializer(serializers.ModelSerializer):
    id = HashIdField(model=models.Reservation)
    user = UserSerializer()

    class Meta:
        model = models.Reservation
        exclude = []


class ChargeTypeSerializer(serializers.ModelSerializer):
    id = HashIdField(model=models.ChargeType)

    class Meta:
        model = models.ChargeType
        exclude = []
