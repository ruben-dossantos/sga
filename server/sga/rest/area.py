# coding=utf-8

import django_filters
from rest_framework import viewsets, permissions, serializers
from sga.models import Area


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area


class AreaReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        depth = 1


class AreaViewSet(viewsets.ModelViewSet):
    model = Area
    queryset = Area.objects.all()
    filter_fields = ['store']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AreaReadSerializer
        return AreaSerializer