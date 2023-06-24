from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        verbose_name='First Name',
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=30,
        null=False,
        blank=False,
    )

    image = models.URLField(
        null=False,
        blank=False,
    )


class Book(models.Model):
    title = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    image = models.URLField(
        null=False,
        blank=False,
    )

    type = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
