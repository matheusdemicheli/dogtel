from django.contrib import admin
from reservation.models import Reservation
from reservation.forms import ReservationForm


class ReservationAdmin(admin.ModelAdmin):
    """
    Reservation ModelAdmin.
    """
    form = ReservationForm
    autocomplete_fields = ['dog']


admin.site.register(Reservation, ReservationAdmin)