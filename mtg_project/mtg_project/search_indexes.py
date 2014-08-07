import datetime
from haystack import indexes
from mtg_project.models import MagicCard, MagicSet, MagicType, MagicSubtype

class MagicCardIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document= True, use_template = True)

    name = indexes.CharField(model_attr = 'card_name')
    set = indexes.CharField(model_attr = 'card_setID__set_name')
    type = indexes.CharField(model_attr = 'card_type__type_name')
    subtype = indexes.CharField(model_attr = 'card_subtype__subtype_name', null = True)
    ctext = indexes.CharField(model_attr = 'card_text')
    ftext = indexes.CharField(model_attr = 'card_flavor_text')

    def get_model(self):
        return MagicCard

    def index_queryset(self, using=None):
        return self.get_model().objects

class MagicSetIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document= True, use_template = True)

    name = indexes.CharField(model_attr = 'set_name')
    release = indexes.CharField(model_attr = 'set_release_date')
    ID = indexes.CharField(model_attr = 'set_ID')
    details = indexes.CharField(model_attr = 'set_details')
    story = indexes.CharField(model_attr = 'set_story')


    def get_model(self):
        return MagicSet

    def index_queryset(self, using=None):
        return self.get_model().objects

class MagicTypeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document= True, use_template = True)

    name = indexes.CharField(model_attr = 'type_name')
    description = indexes.CharField(model_attr = 'type_description')
    subtypes = indexes.MultiValueField()

    def get_model(self):
        return MagicType

    def index_queryset(self, using=None):
        return self.get_model().objects

    def prepare_subtypes(self, obj) :
        return [subtype.subtype_name for subtype in obj.type_subtypes.all()]