from django.contrib import admin

from .models import Task


admin.site.register(Task)

class TodoAdmin(admin.ModelAdmin):
   display = ['title']