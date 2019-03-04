from django.urls import re_path, path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # re_path('^search/$', views.haystack_search, name='search'),
    path('order_list', views.order_list, name='order_list'),
    path('archives_list', views.archives_list, name='archives_list'),
    path('details/<int:question_id>', views.order_detail, name='order_detail'),
    path('results/<int:question_id>', views.results, name='results'),
    path('vote/<int:question_id>', views.vote, name='vote'),
]