# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from . import seriazlizers, models
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
# Create your views here.


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = seriazlizers.DepartmentSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = models.Manufacturer.objects.all()
    serializer_class = seriazlizers.ManufacturerSerializer


class ReservationTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ReservationType.objects.all()
    serializer_class = seriazlizers.ReservationTypeSerializer


class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = models.Instrument.objects.all()
    serializer_class = seriazlizers.InstrumentSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('department', 'charge_type', 'status', 'manufacturer')


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = models.Reservation.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('instrument', )
    serializer_class = seriazlizers.ReservationSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
