# Generated by Django 5.1.6 on 2025-02-25 17:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manic_app', '0007_nailtechnician_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате: '+375XXXXXXXXX'.", regex='^\\+375\\d{9}$')]),
        ),
        migrations.AlterField(
            model_name='nailtechnician',
            name='phone_number',
            field=models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате: '+375XXXXXXXXX'.", regex='^\\+375\\d{9}$')]),
        ),
    ]
