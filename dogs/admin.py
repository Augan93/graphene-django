from django.contrib import admin
from . import models

@admin.register(models.Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'breed',
    )