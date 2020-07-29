from django import forms
from django.db.models import Q
from reservation.models import Reservation


class ReservationForm(forms.ModelForm):
    """
    Reservation ModelForm.
    """

    class Meta:
        model = Reservation
        fields = '__all__'

    def _clean_check_out(self):
        """
        Validations for field check-out.
        """
        check_in = self.cleaned_data.get('check_in')
        check_out = self.cleaned_data.get('check_out')

        if check_in and check_out and check_in > check_out:
            raise forms.ValidationError('Check-out must be after check-in.')

    def _clean_dates(self):
        """
        Validate that the reservation is not crashing dates with another.
        """
        check_in = self.cleaned_data.get('check_in')
        check_out = self.cleaned_data.get('check_out')

        if check_in and check_out:
            reservations = Reservation.objects.filter(
                Q(
                    check_in__lte=check_in,
                    check_out__gte=check_in
                )
                |
                Q(
                    check_in__lte=check_out,
                    check_out__gte=check_out
                )
                |
                Q(
                    check_in__gt=check_in,
                    check_out__lt=check_out
                )
            )
            if self.instance.pk:
                reservations = reservations.exclude(pk=self.instance.pk)

            if reservations.exists():
                raise forms.ValidationError(
                    'There are others reservations for the same dates.'
                )

    def clean(self):
        """
        General validations.
        """
        self._clean_check_out()
        self._clean_dates()
