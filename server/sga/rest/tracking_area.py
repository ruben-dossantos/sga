# coding=utf-8

import django_filters
from rest_framework import viewsets, permissions, serializers
from sga.models import TrackingArea


class TrackingAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingArea


class TrackingAreaReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingArea
        depth = 1


class TrackingAreaViewSet(viewsets.ModelViewSet):
    model = TrackingArea
    queryset = TrackingArea.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TrackingAreaReadSerializer
        return TrackingAreaSerializer