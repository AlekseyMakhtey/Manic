from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from datetime import datetime, time, timedelta


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')

    phone_regex = RegexValidator(regex=r'^\+375\d{9}$',
                                 message="Номер телефона должен быть в формате: '+375XXXXXXXXX'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=False, null=False)
    #

    # Поле для электронной почты (без значения по умолчанию)
    email = models.EmailField(max_length=254, unique=True, blank=False, null=False)

    address = models.CharField(max_length=200, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

# Остальные модели (NailTechnician, Schedule, Review) остаются без изменений


# В models.py
class NailTechnician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nail_technician_profile', null=True, blank=True)  # Добавляем связь
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(
        validators=[
            RegexValidator(regex=r'^\+375\d{9}$', message="Номер телефона должен быть в формате: '+375XXXXXXXXX'.")],
        max_length=12,  # Установите максимальную длину, соответствующую '+375XXXXXXXXX' (12 символов)
        unique=True
    )
    email = models.EmailField(max_length=254, unique=True)
    SPECIALIZATIONS = [
        ('classic', 'Классический маникюр'),
        ('gel', 'Гелевое наращивание'),
        ('acrylic', 'Акриловое наращивание'),
        ('design', 'Дизайн ногтей'),
    ]
    specialization = models.CharField(max_length=10, choices=SPECIALIZATIONS, default='classic')
    experience_years = models.PositiveIntegerField(help_text="Сколько лет опыта работы")
    rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    work_address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Мастер по маникюру'
        verbose_name_plural = 'Мастера по маникюру'


class WorkPhoto(models.Model):
    technician = models.ForeignKey(NailTechnician, on_delete=models.CASCADE, related_name='work_photos')
    photo = models.ImageField(upload_to='work_photos/', blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Фото работы для {self.technician}"


class Schedule(models.Model):
    technician = models.ForeignKey('NailTechnician', on_delete=models.CASCADE, related_name='schedules')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def clean(self):
        # Проверка, что время начала и конца кратны 15 минутам
        if self.start_time.minute % 15 != 0 or self.end_time.minute % 15 != 0:
            raise ValidationError('Время должно быть кратно 15 минутам')
        # Проверка, что время начала меньше времени конца
        if self.start_time >= self.end_time:
            raise ValidationError('Время начала должно быть раньше времени конца')

    def __str__(self):
        return f"Расписание для {self.technician} с {self.start_time} до {self.end_time}"

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class Review(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='reviews')
    technician = models.ForeignKey('NailTechnician', on_delete=models.CASCADE, related_name='reviews')
    # Исправленное использование валидаторов
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.client.user.username} для {self.technician} - Оценка: {self.rating}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'