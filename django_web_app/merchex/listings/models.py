from django.core import validators
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.fields.related import ForeignKey


# Create your models here.

class Band(models.Model):

    def __str__(self) -> str:
        return f'{self.name}'

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        POP_MUSIC = 'POP'

    class Type(models.TextChoices):
        RECORDS = 'REC'
        CLOTHING = 'CLO'
        POSTERS = 'POS'
        MISCELLANEOUS = 'MIS'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    description = models.fields.CharField(max_length=500, default='Classic Music')


class Listing(models.Model):

    def __str__(self) -> str:
        return f'{self.title}'

    class Type(models.TextChoices):
        RECORDS = 'REC'
        CLOTHING = 'CLO'
        POSTERS = 'POS'
        MISCELLANEOUS = 'MIS'


    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=500, default='Pop Music')
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)], default=1915)
    type = models.fields.CharField(choices=Type.choices, max_length=5, default='MIS')

    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

