import datetime
from haystack import indexes
from mtg_project.models import MagicCard, MagicSet, MagicType, MagicSubtype

class MagicCardIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document= True, use_template = True)

    def get_model(self):
        return MagicCard

    def index_queryset(self, using=None):
        return self.get_model().objects
