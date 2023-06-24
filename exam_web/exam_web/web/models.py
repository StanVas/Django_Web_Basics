from django.core.validators import MinLengthValidator
from django.db import models

from exam_web.web.validators import contains_only_letters, start_with_letter


class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MIN_LEN = 1
    FIRST_NAME_MAX_LEN = 25
    LAST_NAME_MAX_LEN = 35
    EMAIL_MAX_LEN = 40
    PASSWORD_MAX_LEN = 20
    PASSWORD_MIN_LEN = 8
    DEFAULT_AGE = 18

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        verbose_name='First Name',
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            start_with_letter,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        verbose_name='Last Name',
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            start_with_letter,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        max_length=EMAIL_MAX_LEN,
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
        validators=(
            MinLengthValidator(PASSWORD_MIN_LEN),
        ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
        null=True,
        blank=True,
    )

    age = models.PositiveIntegerField(
        default=DEFAULT_AGE,
        null=True,
        blank=True,
    )


class Fruit(models.Model):
    NAME_MIN_LEN = 2
    NAME_MAX_LEN = 30

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            MinLengthValidator(NAME_MIN_LEN),
            contains_only_letters,
        ),
        null=False,
        blank=False,
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

    nutrition = models.TextField(
        null=True,
        blank=True,
    )
