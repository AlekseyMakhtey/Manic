from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import ClientRegistrationForm, NailTechnicianRegistrationForm
from .models import NailTechnician, Schedule, Review  # Добавляем Schedule
import logging

# Настройка логирования для отладки
logger = logging.getLogger(__name__)


def register(request):
    # Оставляем регистрацию клиентов как есть
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('home')
    else:
        form = ClientRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def register_technician(request):
    if request.method == 'POST':
        form = NailTechnicianRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                logger.info(f"User {user.username} saved as NailTechnician")
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                return redirect('home')  # Перенаправление на главную страницу
            except Exception as e:
                logger.error(f"Error saving NailTechnician: {str(e)}")
                return render(request, 'registration/register_technician.html', {
                    'form': form,
                    'error_message': f"Произошла ошибка при регистрации: {str(e)}"
                })
        else:
            logger.error(f"Form is invalid: {form.errors}")
    else:
        form = NailTechnicianRegistrationForm()

    return render(request, 'registration/register_technician.html', {
        'form': form,
    })


def home(request):
    technicians = NailTechnician.objects.all()  # Список мастеров на главной странице
    return render(request, 'home.html', {'technicians': technicians})


def technician_detail(request, technician_id):
    technician = get_object_or_404(NailTechnician, pk=technician_id)
    schedules = Schedule.objects.filter(technician=technician)
    reviews = Review.objects.filter(technician=technician)
    return render(request, 'technician_detail.html', {
        'technician': technician,
        'schedules': schedules,
        'reviews': reviews,
    })