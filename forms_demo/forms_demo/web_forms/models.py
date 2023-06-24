from django.db import models


class Pet(models.Model):
    MAX_NAME_LENGTH = 30
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
    )

    def __str__(self):
        return self.name


class Person(models.Model):
    MAX_NAME_LENGTH = 30
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
    )

    pets = models.ManyToManyField(
        Pet,
    )
