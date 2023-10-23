from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'done']
    search_fields = ['name']
    list_filter = ['done']

# admin.site.register(Task)