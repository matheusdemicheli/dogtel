from django.contrib import admin
from django.utils.safestring import mark_safe
from customer.models import Owner, Dog, Breed, SubBreed

class OwnerAdmin(admin.ModelAdmin):
    """
    Owner ModelAdmin.
    """
    search_fields = ['name']


class BreedAdmin(admin.ModelAdmin):
    """
    Breed ModelAdmin.
    """
    search_fields = ['name']


class SubBreedAdmin(admin.ModelAdmin):
    """
    SubBreed ModelAdmin.
    """
    search_fields = ['name', 'breed__name']
    autocomplete_fields = ['breed']
    list_display = ['name', 'breed']


class DogAdmin(admin.ModelAdmin):
    """
    Dog ModelAdmin.
    """
    search_fields = ['name', 'owner__name']
    autocomplete_fields = ['owner', 'breed', 'sub_breed']
    list_display = ['name', 'owner', 'breed', 'sub_breed', 'img_photo']

    def img_photo(self, obj):
        """
        Render the dog's photo.
        """
        return mark_safe('<img src="%s" width="70">' % obj.photo.url)


admin.site.register(Dog, DogAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Breed, BreedAdmin)
admin.site.register(SubBreed, SubBreedAdmin)