# Generated by Django 5.1.6 on 2025-02-25 17:07

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manic_app', '0006_workphoto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='nailtechnician',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nail_technician_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='nailtechnician',
            name='phone_number',
            field=models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате: '+375ххххххххх'", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
