# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from lims_api import settings


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Manufacturer(models.Model):
    english_name = models.CharField(max_length=1024, blank=True, null=True, unique=True)
    chinese_name = models.CharField(max_length=1024, blank=True, null=True, unique=True)

    def __unicode__(self):
        return self.chinese_name or self.english_name


class ReservationType(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class ChargeType(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Instrument(models.Model):
    INSTRUMENT_STATUS_CHOICES = (
        ('R', 'ready'),
        ('O', 'occupied'),
        ('U', 'unavailable')
    )
    RESERVATION_CHOICES = (
        ('OL', 'online'),
        ('PH', 'phone'),
        ('DL', 'delivery')
    )
    name = models.CharField(max_length=256)
    # todo admin m2m
    status = models.CharField(max_length=64, choices=INSTRUMENT_STATUS_CHOICES, default='R')
    department = models.ForeignKey(Department, blank=True, null=True)
    location = models.CharField(max_length=256, blank=True, null=True)
    image = models.ImageField(upload_to=settings.UPLOAD_FOLDER, max_length=256)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True)
    model = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    application = models.TextField(blank=True, null=True)
    accessories = models.TextField(blank=True, null=True)
    charge_type = models.ForeignKey(ChargeType, null=True)
    # reservation_type = models.CharField(max_length=64, choices=RESERVATION_CHOICES, default="OL")
    reservation_type = models.ManyToManyField(ReservationType)
    reservation_time_unit = models.IntegerField(default=1)
    reservation_start_time = models.TimeField(null=True)
    reservation_end_time = models.TimeField(null=True)
    sci_discount = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Reservation(models.Model):
    instrument = models.ForeignKey(Instrument)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __unicode__(self):
        return self.instrument.name
