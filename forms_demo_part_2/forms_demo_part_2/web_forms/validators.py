from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_text(value):
    if '_' in value:
        raise ValidationError('`_` is invalid character for text!')


def validate_priority(value):
    if value < 1 or 10 < value:
        raise ValidationError('Priority must be between 1 and 10!')


# do the same as validate_priority but with a class, so we don't need to hardcode the values for min and max
class ValueInRangeValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    # make the class callable
    def __call__(self, value):
        if value < self.min_value or self.max_value < value:
            raise ValidationError(f'Value must be between {self.min_value} and {self.max_value}!')


# if we want to use the same methods for validations in Models
# we have to use `@deconstructible` constructor and `__eq__` method
@deconstructible
class ValueInRangeValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    # make the class callable
    def __call__(self, value):
        if value < self.min_value or self.max_value < value:
            raise ValidationError(f'Value must be between {self.min_value} and {self.max_value}!')

    # implement `__eq__` method so we can use this validation in Models
    def __eq__(self, other):
        return (
                isinstance(other, self.__class__)
                and self.min_value == other.min_value
                and self.max_value == other.max_value
        )
