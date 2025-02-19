from django.contrib import admin
from .models import Client, NailTechnician, Schedule, Review


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'email', 'address', 'date_joined')

@admin.register(NailTechnician)
class NailTechnicianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'specialization', 'experience_years', 'rating', 'work_address')

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('technician', 'start_time', 'end_time')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('client', 'technician', 'rating', 'comment', 'created_at')