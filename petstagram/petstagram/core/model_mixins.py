class StrFromFieldsMixin:
    # auto generate __str__ for admin site
    # // use it like this //
    # class Photo(StrFromFieldsMixin, models.Model):
    #     str_fields = ('photo', 'location')
    str_fields = ()

    def __str__(self):
        fields = [(str_field, getattr(self, str_field, None)) for str_field in self.str_fields]
        return ', '.join(f'{name}={value}' for (name, value) in fields)
