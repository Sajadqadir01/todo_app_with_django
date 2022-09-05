from django.contrib import admin
from .models import Task


class MyAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'create']


admin.site.register(Task, MyAdmin)
