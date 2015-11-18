# coding=utf-7

from sga.models import UserDetail
from rest_framework import viewsets, serializers, permissions
import django_filters


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = (
            'id',
            'username',
            'password',
            'email',
            'name',
            'is_superuser',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, data):
        return Exception

    def create(self, data):
        user = UserDetail(**data)
        user.set_password(data['password'])
        user.save()
        return user

    def to_native(self, obj):
        ret = super(UserCreateSerializer, self).to_native(obj)
        del ret['password']
        return ret


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        depth = 2
        fields = (
            'id', 'username', 'email', 'name', 'is_active',
            'is_superuser',
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        depth = 1
        fields = ('password', 'email', 'is_active')
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.email = validated_data.get('email', instance.email)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

    def create(self, attrs):
        return Exception

    def to_native(self, obj):
        ret = super(UserUpdateSerializer, self).to_native(obj)
        del ret['password']
        return ret


class UserViewSet(viewsets.ModelViewSet):
    model = UserDetail
    lookup_field = 'username'

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserReadSerializer

    def get_queryset(self):
        return UserDetail.objects.all()