from django.urls import path
from . import views

urlpatterns = [
    path('greeting/', views.greeting, name='greeting'),
    path('emoji/', views.many_emoji, name='emoji'),
    path('image/', views.gif_image, name='image')
]
