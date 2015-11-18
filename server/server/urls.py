from django.conf.urls import url, include
from rest_framework import routers
from sga.rest.generated import *
from sga.rest.store import StoreViewSet
from sga.rest.promotion import PromotionViewSet
from sga.rest.age_group_promotion import AgeGroupPromotionViewSet
from sga.rest.area import AreaViewSet
from sga.rest.area_promotion import AreaPromotionViewSet
from sga.rest.beacon import BeaconViewSet
from sga.rest.area_beacon import AreaBeaconViewSet
from sga.rest.device import DeviceViewSet
from sga.rest.tracking_area import TrackingAreaViewSet
from sga.rest.user import UserViewSet

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

routees = [
    (r'brands', BrandViewSet),
    (r'locations', LocationViewSet),
    (r'promotion_types', PromotionTypeViewSet),
    (r'age_groups', AgeGroupViewSet),
    (r'stores', StoreViewSet),
    (r'promotions', PromotionViewSet),
    (r'age_group_promotions', AgeGroupPromotionViewSet),
    (r'areas', AreaViewSet),
    (r'area_promotions', AreaPromotionViewSet),
    (r'beacons', BeaconViewSet),
    (r'area_beacons', AreaBeaconViewSet),
    (r'devices', DeviceViewSet),
    (r'tracking_areas', TrackingAreaViewSet),
    (r'users', UserViewSet),
]

for routee in routees:
    router.register(routee[0], routee[1], routee[0])

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
