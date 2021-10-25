#  hello/urls.py

from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('layout', views.home_page_view, name='layout'),
    path('layoutFilho1', views.layout_filho1_page_view, name='layoutFilho1'),
    path('layoutFilho2', views.layout_filho2_page_view, name='layoutFilho2'),
    path('layoutFilho3', views.layout_filho3_page_view, name='layoutFilho3'),
]