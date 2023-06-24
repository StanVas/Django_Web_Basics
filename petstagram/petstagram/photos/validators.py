from django.core.exceptions import ValidationError

from petstagram.core.utils import megabytes_to_bytes


def validate_file_size(file_object):
    file_size = file_object.size
    megabyte_limit = 5.0
    if file_size > megabytes_to_bytes(megabyte_limit):
        raise ValidationError(f'The maximum file size that can be uploaded is {megabyte_limit}MB')
