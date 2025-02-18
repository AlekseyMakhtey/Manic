# Generated by Django 5.1.6 on 2025-02-17 08:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manic_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(default='(venv) PS D:\\PythonProject\\Manic\\Manic> python manage.py makemigrations', max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(default='default@example.com', max_length=17, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате: '+999999999'. Допускается от 9 до 15 цифр.", regex='^\\+?1?\\d{9,15}$')]),
            preserve_default=False,
        ),
    ]
