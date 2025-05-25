from django.shortcuts import render
from . import models
from django.views import generic

# Общий список продуктов
def all_products(request):
    tags = models.Tag.objects.all()
    context = {'tags': tags}
    return render(request, 'hashtags/genre_list.html', context)


    
def movies_by_genre(request, genre_name):
    from tv_show.models import Movies
    movies = Movies.objects.filter(genre_choices=genre_name)
    return render(request, 'hashtags/movies_by_genre.html', {
        'tag_name': genre_name,
        'movies': movies
    })


    
    