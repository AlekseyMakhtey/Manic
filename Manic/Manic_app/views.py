from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ClientRegistrationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу после регистрации
        else:
            # Добавим отладку, чтобы убедиться, что ошибки передаются
            print(form.non_field_errors())
            print(form.errors)
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = ClientRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def home(request):
    return render(request, 'home.html')