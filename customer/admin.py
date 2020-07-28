from django.contrib import admin
from customer.models import Owner, Dog, Breed, SubBreed

# Register your models here.

class OwnerAdmin(admin.ModelAdmin):
    """
    Owner's ModelAdmin.
    """
    search_fields = ['name']


class BreedAdmin(admin.ModelAdmin):
    """
    Breed's ModelAdmin.
    """
    search_fields = ['name']


class SubBreedAdmin(admin.ModelAdmin):
    """
    SubBreed's ModelAdmin.
    """
    list_display = ['name', 'breed']
    search_fields = ['name', 'breed__name']
    autocomplete_fields = ['breed']


class DogAdmin(admin.ModelAdmin):
    """
    Dog's ModelAdmin.
    """
    autocomplete_fields = ['owner', 'breed']


admin.site.register(Dog, DogAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Breed, BreedAdmin)
admin.site.register(SubBreed, SubBreedAdmin)