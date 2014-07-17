from tastypie.resources import ModelResource
from mtg_project.models import MagicCard, MagicSet, MagicType, MagicSubtype

class MagicCardResource(ModelResource):
    class Meta:
        queryset = MagicCard.objects.all()
        resource_name = 'magic_card'

class MagicSetResource(ModelResource):
    class Meta:
        queryset = MagicSet.objects.all()
        resource_name = 'magic_set'

class MagicTypeResource(ModelResource):
    class Meta:
        resource_name = 'magic_type'

class MagicSubtypeResource(ModelResource):
    class Meta:
        resource_name = 'magic_subtype'

