# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(ReservationType)
class ReservationTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(ChargeType)
class ChargeTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(IotClient)
class IotClientAdmin(admin.ModelAdmin):
    pass


@admin.register(InstrumentRecord)
class InstrumentRecordAdmin(admin.ModelAdmin):
    pass


@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):
    pass
