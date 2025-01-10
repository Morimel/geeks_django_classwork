from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tv_show.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)