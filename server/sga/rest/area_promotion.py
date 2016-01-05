# coding=utf-8

import django_filters
from rest_framework import viewsets, permissions, serializers
from sga.models import AreaPromotion


class AreaPromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaPromotion


class AreaPromotionReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaPromotion
        depth = 1


class AreaPromotionViewSet(viewsets.ModelViewSet):
    model = AreaPromotion
    filter_fields = ['area']
    queryset = AreaPromotion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AreaPromotionReadSerializer
        return AreaPromotionSerializer