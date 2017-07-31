# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from . import serializers, models
from rest_framework import permissions
from dynamic_rest.viewsets import DynamicModelViewSet


class UserViewSet(DynamicModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    ordering = ('username',)
