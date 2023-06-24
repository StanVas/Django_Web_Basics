from django.core.exceptions import ValidationError


def start_with_letter(value):
    if value[0].isdigit():
        raise ValidationError("Your name must start with a letter!")


def contains_only_letters(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")
