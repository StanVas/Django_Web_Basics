from django.db import models

from petstagram.photos.models import Photo


class PhotoComment(models.Model):
    # Photo's field for likes is named {NAME_OF_THIS_MODEL.lower()}_set
    # in this case photocomment_set (using this in common\views.py)
    MAX_TEXT_LENGTH = 300

    text = models.TextField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    # when a comment is created (only), the date of publication is automatically generated
    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )


class PhotoLike(models.Model):
    # Photo's field for likes is named {NAME_OF_THIS_MODEL.lower()}_set
    # in this case photolike_set
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    # TODO when we have users
    # user = models.ForeignKey(
    #     User,
    #     on_delete = models.RESTRICT,
    # )
