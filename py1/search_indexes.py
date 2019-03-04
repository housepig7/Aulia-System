from haystack import indexes
from .models import *


class OrderIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Order

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class OrderPpIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return OrderPp

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class ArchivesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Archives

    def index_queryset(self, using=None):
        return self.get_model().objects.all()