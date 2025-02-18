from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')

    # Валидация номера телефона, пример для международного формата
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Номер телефона должен быть в формате: '+375ххххххххх'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=False, null=False)

    # Поле для электронной почты
    email = models.EmailField(max_length=254, unique=True, blank=False, null=False, default='default@example.com')

    address = models.CharField(max_length=200, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'