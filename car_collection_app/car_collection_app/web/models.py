from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from car_collection_app.web.validators import validate_year


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(2),
        ),
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(18),
        ),
    )

    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        verbose_name='First Name',
        max_length=30,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=30,
        null=True,
        blank=True,
    )

    profile_picture = models.CharField(
        verbose_name='Profile Picture',
        null=True,
        blank=True,
    )


class Car(models.Model):
    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    CAR_TYPE = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    type = models.CharField(
        max_length=10,
        choices=CAR_TYPE,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(2),
        ),
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            validate_year,
        ),
    )

    image_url = models.URLField(
        verbose_name='Image URL',
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(1),
        ),
    )
