from django.utils import dateparse
from django.db.models import Avg, Count, Max
from rest_framework import views
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import exceptions
from sga.models import Promotion, AgeGroup, AgeGroupPromotion, Area, AreaPromotion
from sga.rest.permissions import AdminWritePermissions


class PromotionFilterView(views.APIView):
    authentication_classes = (authentication.TokenAuthentication,
                              authentication.SessionAuthentication,
                              authentication.BasicAuthentication)
    permission_classes = (AdminWritePermissions,)


    def get(self, request):
        if not request.user.is_authenticated():
            raise exceptions.NotAuthenticated()

        self.user = request.user
        self.params = request.query_params
        return Response(self.process_promotions())

    def process_promotions(self):
        json = {}
        promotions = Promotion.objects.all()
        age = self.params.get('age')
        promotion_type = self.params.get('promotion_type')
        area = self.params.get('area')

        if promotion_type:
            promotions = promotions.filter(promotion_type=promotion_type)

        for area_promotion in AreaPromotion.objects.filter(area=area):
            for age_group_promotion in AgeGroupPromotion.objects.filter(age_group__age_min__lte=age).filter(age_group__age_max__gte=age):
                if age_group_promotion.promotion.id == area_promotion.promotion.id:
                    promotion = promotions.get(id=area_promotion.promotion.id)
                    print(promotion.name)
        return json


    def process_stores(self, stats):
        json_data = []
        parent = self.params.get('store')
        for store in Store.objects.filter(parent=parent):
            area_max = stats.filter(area__store=store).aggregate(Max('area'))['area__max']
            area = Area.objects.get(id=area_max)
            json = {
                'store': {
                    'id': store.id,
                    'name': store.name,
                    'best_area' : {'id': area.id, 'name': area.name},
                    'nr_of_devices': stats.filter(area__store=store).annotate(Count('device', distinct=True)).count(),
                    'best_day': self.get_max_day(stats.filter(area__store=store)),
                    'best_age': self.get_best_age(stats.filter(area__store=store))
                }
            }
            json_data.append(json)
        return json_data
