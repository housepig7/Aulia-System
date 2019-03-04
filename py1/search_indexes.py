from haystack import indexes
from .models import Order


class OrderIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Order

    def index_queryset(self, using=None):
        return self.get_model().objects.all()