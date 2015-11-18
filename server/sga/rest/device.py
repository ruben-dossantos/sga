# coding=utf-8

import django_filters
from rest_framework import viewsets, permissions, serializers
from sga.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device


class DeviceReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        depth = 1


class DeviceViewSet(viewsets.ModelViewSet):
    model = Device
    queryset = Device.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DeviceReadSerializer
        return DeviceSerializer