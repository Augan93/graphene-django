from django.contrib import admin
from . import models


@admin.register(models.Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'year',
    )
