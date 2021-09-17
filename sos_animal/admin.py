from django.contrib import admin

from sos_animal.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'description', 'user']
