from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
    )

    description = models.TextField()

    priority = models.IntegerField()
