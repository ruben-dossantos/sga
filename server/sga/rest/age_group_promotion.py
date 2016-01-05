# coding=utf-8

import django_filters
from rest_framework import viewsets, permissions, serializers
from sga.models import AgeGroupPromotion


class AgeGroupPromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeGroupPromotion


class AgeGroupPromotionReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeGroupPromotion
        depth = 1


class AgeGroupPromotionViewSet(viewsets.ModelViewSet):
    model = AgeGroupPromotion
    filter_fields = ['age_group']
    queryset = AgeGroupPromotion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AgeGroupPromotionReadSerializer
        return AgeGroupPromotionSerializer