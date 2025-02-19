from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Manic_app.urls')),  # Предполагая, что вы назвали ваше приложение 'Manic_app'
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)