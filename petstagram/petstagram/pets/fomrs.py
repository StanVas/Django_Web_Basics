from django import forms

from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']

        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Link to Image',
            'date_of_birth': 'Date of Birth',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            )
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class DisabledFieldsMixin:
    disabled_fields = ()
    fields = None

    def _disable_fields(self):
        for field_name in self.disabled_fields:
            if field_name in self.fields:
                field = self.fields[field_name]
                field.widget.attrs['disabled'] = 'disabled'  # disabled or readonly depends on the
                field.widget.attrs['readonly'] = 'readonly'  # different fields and their input


class PetDeleteForm(DisabledFieldsMixin, PetBaseForm):
    disabled_fields = ('name', 'date_of_birth', 'personal_photo',)

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print(self.__dict__)  # we can see fields dict inside
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
