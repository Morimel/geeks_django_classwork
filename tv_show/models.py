from django.db import models

class Movies(models.Model):
    GENRE_CHOICES = (
        ('Horror', 'Horror'),
        ('Comedy', 'Comedy'),
        ('Romance', 'Romance'),
    )
    image = models.ImageField(upload_to='movies/', verbose_name='load photo')
    title = models.CharField(max_length=100, verbose_name='name of the movie')
    description = models.TextField(verbose_name='description', blank=True)
    price = models.PositiveIntegerField(verbose_name='price', default=400)
    created_at = models.DateTimeField(auto_now_add=True)
    genre_choices = models.CharField(max_length=100, choices=GENRE_CHOICES, verbose_name='genre')
    time_watch = models.PositiveIntegerField(default=120, verbose_name='duartion')
    director = models.CharField(max_length=100, verbose_name='director')
    trailer = models.URLField(verbose_name='YouTube trailer')
    
    class Meta:
        verbose_name = 'Movies'
        verbose_name_plural = 'Movies'
        
    def __str__(self):
        return f'{self.title}: {self.price} som'
    
    
class Reviews(models.Model):
    STARS = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
    )
    reviews_choice = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='movies')
    created_at = models.DateField(auto_now_add=True)
    comment = models.TextField()
    stars = models.CharField(max_length=100, choices=STARS, default='⭐⭐⭐⭐⭐')
    
    def __str__(self):
        return f'{self.comment}-{self.stars}'