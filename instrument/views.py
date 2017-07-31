# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from . import seriazlizers, models
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from dynamic_rest.viewsets import DynamicModelViewSet


class DepartmentViewSet(DynamicModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = seriazlizers.DepartmentSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

    ordering = ('name',)


class ManufacturerViewSet(DynamicModelViewSet):
    queryset = models.Manufacturer.objects.all()
    serializer_class = seriazlizers.ManufacturerSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

    ordering = ('english_name', 'chinese_name')


class ReservationTypeViewSet(DynamicModelViewSet):
    queryset = models.ReservationType.objects.all()
    serializer_class = seriazlizers.ReservationTypeSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

    ordering = ('name',)


class InstrumentViewSet(DynamicModelViewSet):
    queryset = models.Instrument.objects.all()
    serializer_class = seriazlizers.InstrumentSerializer
    #filter_backends = (DjangoFilterBackend,)
    filter_fields = ('department', 'charge_type', 'status', 'manufacturer')
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

    ordering = ('name', )


class ReservationViewSet(DynamicModelViewSet):
    queryset = models.Reservation.objects.all()
    #filter_backends = (DjangoFilterBackend,)
    filter_fields = ('instrument',)
    serializer_class = seriazlizers.ReservationSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    ordering = ('start_time',)
