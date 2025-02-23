from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Client
from django.core.validators import RegexValidator


class ClientRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=17, required=True, validators=[
        RegexValidator(regex=r'^\+?1?\d{13,14}$', message="Номер телефона должен быть в формате: '+375ххххххххх'.")])
    address = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Это имя пользователя уже занято.")
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError("Пароль должен содержать минимум 8 символов.")
        return password1

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот email уже зарегистрирован.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.startswith('+375'):
            raise forms.ValidationError("Номер телефона должен начинаться с '+375'.")
        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        errors = {}

        if not username:
            errors['username'] = "Имя пользователя обязательно."
        elif User.objects.filter(username=username).exists():
            errors['username'] = "Это имя пользователя уже занято."

        if not email:
            errors['email'] = "Email обязателен."
        elif not '@' in email or not '.' in email.split('@')[1]:
            errors['email'] = "Введите корректный email-адрес."
        elif User.objects.filter(email=email).exists():
            errors['email'] = "Этот email уже зарегистрирован."

        if not phone_number:
            errors['phone_number'] = "Номер телефона обязателен."
        elif not phone_number.startswith('+375'):
            errors['phone_number'] = "Номер телефона должен начинаться с '+375'."

        if not password1:
            errors['password1'] = "Пароль обязателен."
        elif len(password1) < 8:
            errors['password1'] = "Пароль должен содержать минимум 8 символов."

        if not password2:
            errors['password2'] = "Подтверждение пароля обязательно."
        elif password1 and password2 and password1 != password2:
            self.add_error(None, "Пароли не совпадают.")  # Общая ошибка

        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data

    def save(self, commit=True):
        user = super(ClientRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        client = Client.objects.create(user=user,
                                       phone_number=self.cleaned_data['phone_number'],
                                       email=self.cleaned_data['email'],
                                       address=self.cleaned_data.get('address', ''))
        return user