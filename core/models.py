# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=64, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)

    def get_full_name_cn(self):
        return self.last_name + self.first_name

    def __unicode__(self):
        return self.get_full_name_cn() or str(self.username)