from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.urls import include
from website import settings
from apps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
