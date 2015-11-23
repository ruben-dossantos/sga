# coding=utf-7

from sga.models import UserDetail, Image
from rest_framework import viewsets, permissions, serializers

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image

class ImageViewSet(viewsets.ModelViewSet):
    model = Image
    serializer_class = ImageSerializer
    queryset = Image.objects.all()