from rest_framework import serializers
from . import models
from core.models import User
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField
from dynamic_rest.fields import CountField, DynamicMethodField


class UserSerializer(DynamicModelSerializer):
    reservation_set = DynamicRelationField('ReservationSerializer', many=True)

    class Meta:
        model = User
        exclude = []


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
    reservation_set = DynamicRelationField(
        'ReservationSerializer',
        many=True,
        deferred=True
    )
    reservation_count = CountField('reservation_set', deferred=True)
    #
    # def get_user_reservation_count(self, instrument):
    #     return len(instrument.reservation_set.all())

    class Meta:
        model = models.Instrument
        exclude = []


class ReservationSerializer(DynamicModelSerializer):
    user = DynamicRelationField('UserSerializer')

    class Meta:
        model = models.Reservation
        exclude = []
        # deferred_fields = ('user', )


class ChargeTypeSerializer(DynamicModelSerializer):
    class Meta:
        model = models.ChargeType
        exclude = []


# Aggregation serializer
class AggSer(serializers.ModelSerializer):
    pass
