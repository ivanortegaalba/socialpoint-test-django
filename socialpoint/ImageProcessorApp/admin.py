from django.contrib import admin
from ImageProcessorApp.models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=('name','uploaded','image','status')
    list_instances = True
    search_fields = ['name']
