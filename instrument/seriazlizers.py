from rest_framework import serializers
from . import models
from core.serializer import UserSerializer
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

    admin = DynamicRelationField('UserSerializer', embed=True)
    manufacturer = DynamicRelationField('ManufacturerSerializer', embed=True)
    department = DynamicRelationField('DepartmentSerializer', embed=True)
    charge_type = DynamicRelationField('ChargeTypeSerializer', embed=True)
    reservation_type = DynamicRelationField('ReservationTypeSerializer', many=True, embed=True)

    class Meta:
        model = models.Instrument
        exclude = []


class ReservationSerializer(DynamicModelSerializer):
    user = DynamicRelationField('UserSerializer', embed=True)

    class Meta:
        model = models.Reservation
        exclude = []
        #deferred_fields = ('user', )


class ChargeTypeSerializer(DynamicModelSerializer):

    class Meta:
        model = models.ChargeType
        exclude = []
