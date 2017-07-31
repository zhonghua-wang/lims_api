from rest_framework import serializers
from . import models
from core.serializers import UserSerializer
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField


class DepartmentSerializer(DynamicModelSerializer):

    class Meta:
        model = models.Department
        exclude = []


class ManufacturerSerializer(DynamicModelSerializer):

    class Meta:
        model = models.Manufacturer
        exclude = []


class ReservationTypeSerializer(DynamicModelSerializer):

    class Meta:
        model = models.ReservationType
        exclude = []


class ChargeTypeSerializer(DynamicModelSerializer):

    class Meta:
        model = models.ChargeType
        exclude = []


class InstrumentSerializer(DynamicModelSerializer):

    admin = DynamicRelationField('UserSerializer')
    manufacturer = DynamicRelationField('ManufacturerSerializer')
    department = DynamicRelationField('DepartmentSerializer')
    charge_type = DynamicRelationField('ChargeTypeSerializer')
    reservation_type = DynamicRelationField('ReservationTypeSerializer', many=True)

    class Meta:
        model = models.Instrument
        exclude = []


class ReservationSerializer(DynamicModelSerializer):
    user = DynamicRelationField('UserSerializer')

    class Meta:
        model = models.Reservation
        exclude = []
        #deferred_fields = ('user', )


class ChargeTypeSerializer(DynamicModelSerializer):

    class Meta:
        model = models.ChargeType
        exclude = []
