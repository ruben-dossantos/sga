# coding=utf-8

import django_filters
from rest_framework import viewsets, permissions, serializers
from sga.models import AreaBeacon


class AreaBeaconSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaBeacon


class AreaBeaconReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaBeacon
        depth = 1


class AreaBeaconViewSet(viewsets.ModelViewSet):
    model = AreaBeacon
    queryset = AreaBeacon.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AreaBeaconReadSerializer
        return AreaBeaconSerializer