from django.urls import re_path,path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/<str:search_value>', views.search, name='search'),
    path('order_list', views.order_list, name='order_list'),
    path('archives_list', views.archives_list, name='archives_list'),
    path('<int:question_id>/details', views.order_detail, name='order_detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]