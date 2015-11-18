# coding=utf-8

import django_filters
from rest_framework import viewsets, permissions, serializers
from sga.models import Promotion


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion


class PromotionReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        depth = 1


class PromotionViewSet(viewsets.ModelViewSet):
    model = Promotion
    queryset = Promotion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PromotionReadSerializer
        return PromotionSerializer