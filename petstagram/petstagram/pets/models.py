from django.db import models
from django.utils.text import slugify


class Pet(models.Model):
    MAX_NAME = 30

    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
    )

    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        # editable=False,    # if we don't want to edit it from the admin site(will hide the field)
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    # Overrides `save` method so we can auto create slugs for each model(when we create it)
    def save(self, *args, **kwargs):
        # Create/Update (create, so we can have 'id')
        super().save(*args, **kwargs)

        if not self.slug:  # use the 'id'
            self.slug = slugify(f'{self.id}-{self.name}')

        # Update
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'ID={self.id} ; Name={self.name}'
