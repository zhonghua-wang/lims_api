# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from . import seriazlizers, models
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin


class DepartmentViewSet(SerializerExtensionsAPIViewMixin, viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = seriazlizers.DepartmentSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = models.Manufacturer.objects.all()
    serializer_class = seriazlizers.ManufacturerSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class ReservationTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ReservationType.objects.all()
    serializer_class = seriazlizers.ReservationTypeSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = models.Instrument.objects.all()
    serializer_class = seriazlizers.InstrumentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('department', 'charge_type', 'status', 'manufacturer')
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = models.Reservation.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('instrument',)
    serializer_class = seriazlizers.ReservationSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
