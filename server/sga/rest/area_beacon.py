# coding=utf-8

import django_filters
from rest_framework import viewsets, permissions, serializers
from sga.models import AreaBeacon


class AreaBeaconFilter(django_filters.FilterSet):
    beacon = django_filters.MethodFilter(action='beacon_filter')

    class Meta:
        model = AreaBeacon
        fields = ['beacon']

    def beacon_filter(self, queryset, value):
        return queryset.filter(
            beacon__uuid=value
        )


class AreaBeaconSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaBeacon


class AreaBeaconReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaBeacon
        depth = 1


class AreaBeaconViewSet(viewsets.ModelViewSet):
    model = AreaBeacon
    filter_class = AreaBeaconFilter
    queryset = AreaBeacon.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AreaBeaconReadSerializer
        return AreaBeaconSerializer
