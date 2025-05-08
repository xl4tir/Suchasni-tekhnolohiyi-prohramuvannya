from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import article_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/<slug:slug>/', article_detail, name='article_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
