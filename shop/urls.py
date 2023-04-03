from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Shop URLs
    path('shops/create/', views.create_shop, name='shop_create'),
    path('shops/<int:pk>/update/', views.update_shop, name='shop_update'),
    path('', views.shop_list, name='shop_list'),

    # Shop within distance URLs
    path('shops/within_distance/', views.shop_within_distance, name='shop_within_distance'),
    path('shops/within_distance/results/', views.shop_within_distance, name='shop_within_distance_form'),
]
