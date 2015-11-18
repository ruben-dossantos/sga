# coding=utf-8
from rest_framework import viewsets, serializers
from sga.models import Brand, Location, AgeGroup, PromotionType

def queryset(self):
    return self.model.objects.all()

meta_models = [
    dict(
        models=[Brand, Location, AgeGroup, PromotionType],
        get_queryset=queryset
    ),
]

for meta_model in meta_models:
    attr = meta_model.copy()
    del attr['models']
    for m in meta_model['models']:
        attr['model'] = m

        # If no queryset is defined, use default one (access everything)
        if 'get_queryset' not in meta_model:
            attr['queryset'] = attr['model'].objects.all()

        # If no serializer class is defined, use default one
        if 'get_serializer_class' not in meta_model:
            class_name = attr['model'].__name__
            klass = """
class %sSerializer(serializers.ModelSerializer):
    class Meta:
        model = %s
""" % (class_name, class_name)
            exec(klass, globals())
            attr['serializer_class'] = globals()['%sSerializer' % class_name]

        class GenericMeta:
            model = m

        globals()[m.__name__ + 'ViewSet'] = type(
            m.__name__ + 'ViewSet',
            (viewsets.ModelViewSet,),
            attr
        )