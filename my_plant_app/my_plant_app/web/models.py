from django.core.validators import MinLengthValidator
from django.db import models

from my_plant_app.web.validators import validate_capitalized, contains_only_letters


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(2),
        ),
    )

    first_name = models.CharField(
        max_length=20,
        verbose_name='First Name',
        null=False,
        blank=False,
        validators=(
            validate_capitalized,
        ),
    )

    last_name = models.CharField(
        max_length=20,
        verbose_name='Last Name',
        null=False,
        blank=False,
        validators=(
            validate_capitalized,
        ),
    )

    profile_picture = models.URLField(
        verbose_name='Profile Picture',
        null=True,
        blank=True,
    )


class Plant(models.Model):
    OUTDOOR_PLANTS = 'Outdoor Plants'
    INDOOR_PLANTS = 'Indoor Plants'

    PLANTS = (
        (OUTDOOR_PLANTS, OUTDOOR_PLANTS),
        (INDOOR_PLANTS, INDOOR_PLANTS),
    )

    plant_type = models.CharField(
        max_length=14,
        choices=PLANTS,
        verbose_name='Type',
        null=False,
        blank=False,
    )

    name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(2),
            contains_only_letters,
        ),
    )

    image_url = models.URLField(
        verbose_name='Image URL',
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )
