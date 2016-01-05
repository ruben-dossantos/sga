# coding=utf-8

import django_filters
from rest_framework import viewsets, permissions, serializers
from sga.models import Store, UserDetail


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store


class StoreReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        depth = 1

    class StoreUserReadSerializer(serializers.ModelSerializer):
        class Meta:
            model = UserDetail
            depth = 2
            fields = (
                'id', 'username', 'email', 'name', 'is_active',
                'is_superuser',
            )

    user = StoreUserReadSerializer()


class StoreViewSet(viewsets.ModelViewSet):
    model = Store
    filter_fields = ['parent']
    queryset = Store.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StoreReadSerializer
        return StoreSerializer