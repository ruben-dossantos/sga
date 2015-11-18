# coding=utf-8

import django_filters
from rest_framework import viewsets, permissions, serializers
from sga.models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store


class StoreReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        depth = 1


class StoreViewSet(viewsets.ModelViewSet):
    model = Store
    queryset = Store.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StoreReadSerializer
        return StoreSerializer