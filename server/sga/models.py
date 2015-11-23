# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
from django.db import models
from server.settings import UPLOAD_TO_IMAGES

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class UserDetail(AbstractUser):
    SC_ADMIN = 2
    S_ADMIN = 3

    UserTypes = (
        (SC_ADMIN, 'Shopping Center Admin'),
        (S_ADMIN, 'Store Admin'),
    )

    name = models.CharField(max_length=50)
    user_type = models.IntegerField(choices=UserTypes, blank=True, null=True)

class Store(models.Model):
    name = models.CharField(max_length=30)
    brand = models.ForeignKey(Brand, blank=True, null=True,
                              on_delete=models.PROTECT)
    location = models.ForeignKey(Location, blank=True, null=True,
                                 on_delete=models.PROTECT)
    parent = models.ForeignKey('self', blank=True, null=True,
                               on_delete=models.PROTECT)
    user = models.ForeignKey(UserDetail, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.name

class PromotionType(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class AgeGroup(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to=UPLOAD_TO_IMAGES, blank=True, null=True)

class Promotion(models.Model):
    name = models.CharField(max_length=100)
    promo_code = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    image = models.ForeignKey(Image, blank=True, null=True,
                             on_delete=models.PROTECT)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_flash_promotion = models.BooleanField(default=False)
    promotion_type = models.ForeignKey(PromotionType, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.name

class AgeGroupPromotion(models.Model):
    age_group = models.ForeignKey(AgeGroup, on_delete=models.PROTECT)
    promotion = models.ForeignKey(Promotion, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('age_group', 'promotion')

class Area(models.Model):
    name = models.CharField(max_length=30)
    store = models.ForeignKey(Store, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.name

class AreaPromotion(models.Model):
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    promotion = models.ForeignKey(Promotion, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('area', 'promotion')

class Beacon(models.Model):
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    uuid = models.CharField(max_length=100)

    def __unicode__(self):
        return self.uuid

class AreaBeacon(models.Model):
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    beacon = models.ForeignKey(Beacon, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('area', 'beacon')

class Device(models.Model):
    identifier = models.CharField(max_length=100)
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()

class TrackingArea(models.Model):
    device = models.ForeignKey(Device, on_delete=models.PROTECT)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()