from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Manic_app.urls')),  # Предполагая, что вы назвали ваше приложение 'Manic_app'
]