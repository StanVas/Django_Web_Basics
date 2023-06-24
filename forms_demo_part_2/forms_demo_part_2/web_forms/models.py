from django.db import models

from forms_demo_part_2.web_forms.validators import validate_text, ValueInRangeValidator


class Person(models.Model):
    MAX_NAME_LEN = 30
    name = models.CharField(
        max_length=MAX_NAME_LEN,
    )

    profile_image = models.ImageField(
        upload_to='persons',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Todo(models.Model):
    MAX_LEN_TEXT = 30
    MAX_TODOS_PER_PERSON = 3

    text = models.CharField(
        max_length=MAX_LEN_TEXT,
        validators=(
            validate_text,
        ),
        null=False,
        blank=False,
    )

    priority = models.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
        ),
        null=False,
        blank=False,
    )

    is_done = models.BooleanField(
        null=False,
        blank=False,
        default=False,
    )

    assignee = models.ForeignKey(
        Person,
        on_delete=models.RESTRICT,
    )
