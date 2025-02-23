from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Добавляем импорт

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),  # URL для главной страницы
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]
