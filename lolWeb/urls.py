
from django.urls import path
from . import views

urlpatterns = [
    path('', views.champion_list, name='champion_list'),
    path('champion/<str:champion_id>/', views.champion_detail, name='champion_detail'),
]
