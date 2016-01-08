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

class PromotionFilter(django_filters.FilterSet):
    age = django_filters.MethodFilter(action='age_filter')
    area = django_filters.MethodFilter(action='area_filter')
    promotion_type = django_filters.MethodFilter(action='promotion_type_filter')

    class Meta:
        model = Promotion

    def age_filter(self, queryset, value):
        return queryset.filter(agegrouppromotion__age_group__age_min__lte=value).filter(agegrouppromotion__age_group__age_max__gte=value)

    def area_filter(self, queryset, value):
        return queryset.filter(areapromotion__area=value)

    def promotion_type_filter(self, queryset, value):
        return queryset.filter(promotion_type=value)

class PromotionViewSet(viewsets.ModelViewSet):
    model = Promotion
    filter_class = PromotionFilter
    queryset = Promotion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PromotionReadSerializer
        return PromotionSerializer