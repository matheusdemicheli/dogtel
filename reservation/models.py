from django.db import models
from customer.models import Dog

# Create your models here.

class Reservation(models.Model):
    """
    Representation of a reservation in hotel.
    """

    check_in = models.DateTimeField(verbose_name='Check-in')

    check_out = models.DateTimeField(verbose_name='Check-out')

    dog = models.ForeignKey(to=Dog, on_delete=models.PROTECT)

    def __str__(self):
        return '%s: %s - %s' % (self.dog, self.check_in, self.check_out)
