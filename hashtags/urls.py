from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('genre/<str:genre_name>/', views.movies_by_genre, name='movies_by_genre'),
]
