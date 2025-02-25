from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('technician/<int:technician_id>/', views.technician_detail, name='technician_detail'),
    path('register/', views.register, name='register'),  # Регистрация клиентов
    path('register/technician/', views.register_technician, name='register_technician'),  # Регистрация мастеров
]