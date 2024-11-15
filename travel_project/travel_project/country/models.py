from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class ContinentChoices(models.TextChoices):
    AFRICA = 'Africa', 'Africa'
    ASIA = 'Asia', 'Asia'
    EUROPE = 'Europe', 'Europe'
    NORTH_AMERICA = 'North America', 'North America'
    SOUTH_AMERICA = 'South America', 'South America'
    AUSTRALIA_AND_OCEANIA = 'Australia and Oceania', 'Australia and Oceania'
    ANTARCTICA = 'Antarctica', 'Antarctica'


class Country(models.Model):
    name = models.CharField(max_length=50)
    continent = models.CharField(
        max_length=40,
        choices=ContinentChoices.choices
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    capital = models.CharField(max_length=100)
    population = models.PositiveBigIntegerField()
    official_language = models.CharField(max_length=100)
    currency = models.CharField(max_length=50)
    is_visited = models.BooleanField(default=False)

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

