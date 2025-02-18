from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ClientRegistrationForm

def register(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Замените 'home' на URL, куда вы хотите перенаправить пользователя после регистрации
    else:
        form = ClientRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})