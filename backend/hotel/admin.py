from django.contrib import admin
from .models import Job, Service

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "location", "job_type", "work_mode", "created_at")
    search_fields = ("title", "company", "location", "job_type", "skills")
    list_filter = ("job_type", "work_mode", "location")
    ordering = ("-created_at",)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "service_type", "location", "phone", "price_from")
    search_fields = ("name", "location", "service_type", "description")
    list_filter = ("service_type", "location")
