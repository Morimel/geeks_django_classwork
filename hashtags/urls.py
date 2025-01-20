from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('eat_products/', views.eat_products, name='eat_products'),
    path('drink_products/', views.DrinkProductsView.as_view(), name='drink_products'),
]
