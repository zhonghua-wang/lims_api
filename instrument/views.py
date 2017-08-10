# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from django.db.models import Count

from . import serializers, models
from core.models import User
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from dynamic_rest.viewsets import DynamicModelViewSet
from datetime import datetime

class UserViewSet(DynamicModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    ordering = ('username',)


class DepartmentViewSet(DynamicModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

    ordering = ('name',)


class ManufacturerViewSet(DynamicModelViewSet):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

    ordering = ('english_name', 'chinese_name')


class ReservationTypeViewSet(DynamicModelViewSet):
    queryset = models.ReservationType.objects.all()
    serializer_class = serializers.ReservationTypeSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

    ordering = ('name',)


class InstrumentViewSet(DynamicModelViewSet):
    queryset = models.Instrument.objects.all()
    serializer_class = serializers.InstrumentSerializer
    # filter_backends = (DjangoFilterBackend,)
    filter_fields = ('department', 'charge_type', 'status', 'manufacturer')
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

    ordering = ('name',)


class ReservationViewSet(DynamicModelViewSet):
    queryset = models.Reservation.objects.all()
    # filter_backends = (DjangoFilterBackend,)
    filter_fields = ('instrument',)
    serializer_class = serializers.ReservationSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    ordering = ('start_time',)


# aggregation
class InstrumentReservationStatistic(generics.ListAPIView):
    queryset = models.Reservation.objects \
        .filter(instrument_id=5) \
        .values('user') \
        .annotate(reservation_count=Count('user'))
    serializer_class = serializers.InstrumentUserReservationCount
    permission_classes = (permissions.AllowAny,)


# iot apis
class iot_view(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = request.POST
        card_id = data.get('card_id')
        iot_id = int(data.get('iot_id'))
        print card_id, iot_id

        iot_client = models.IotClient.objects.get(id=iot_id)
        user = User.objects.get(card_id=card_id)
        instrument = iot_client.instrument
        # instrument is ready for using
        if instrument.status == 'R':
            # reservation is needed
            if instrument.need_reservation and not instrument.is_valid_reservation(user=user):
                return Response("D")  # return 'D' back to client, which mean deny the request
            else:
                # new instrument record
                record = models.InstrumentRecord.objects.create(
                    instrument=instrument,
                    user=user,
                    start_time=datetime.now()
                )
        else:
            return Response('OK')
