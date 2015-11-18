# coding=utf-8

import django_filters
from rest_framework import viewsets, permissions, serializers
from sga.models import Beacon


class BeaconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beacon


class BeaconReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beacon
        depth = 1


class BeaconViewSet(viewsets.ModelViewSet):
    model = Beacon
    queryset = Beacon.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BeaconReadSerializer
        return BeaconSerializer