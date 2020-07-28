from django.db import models

# Create your models here.

class Owner(models.Model):
    """
    Representation of the Owner of a Dog.
    """
    name = models.CharField(max_length=50)

    phone = models.CharField(max_length=11)

    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'

    def __str__(self):
        return self.name


class Breed(models.Model):
    """
    Representation of a dog's breed.
    """
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Breed"
        verbose_name_plural = "Breeds"

    def __str__(self):
        return self.name


class SubBreed(models.Model):
    """
    Representation of a dog's sub-breed.
    """
    name = models.CharField(max_length=30)

    breed = models.ForeignKey(
        to=Breed,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Sub-Breed"
        verbose_name_plural = "Sub-Breeds"

    def __str__(self):
        return self.name


class Dog(models.Model):
    """
    Representation of a dog.
    """
    name = models.CharField(max_length=30)

    breed = models.ForeignKey(
        to=Breed,
        on_delete=models.PROTECT
    )

    owner = models.ForeignKey(
        to=Owner,
        on_delete=models.PROTECT
    )

    observation = models.TextField(
        null=True,
        blank=True,
        help_text='Special treatment, medicines, etc.'
    )

    class Meta:
        verbose_name = 'Dog'
        verbose_name_plural = 'Dogs'

    def __str__(self):
        return self.name
