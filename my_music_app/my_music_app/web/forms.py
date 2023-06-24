from django import forms

from my_music_app.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ()  # instead of hiding the fields we just don't show them at first place

    # def __int__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Album.objects.all().delete()
            self.instance.delete()
        return self.instance

    # def __set_hidden_fields(self):
    #     for _, field in self.fields.items():
    #         field.widget = forms.HiddenInput()


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
        }


class CreateAlbumForm(BaseAlbumForm):
    pass


class EditAlbumForm(BaseAlbumForm):
    pass


class DeleteAlbumForm(BaseAlbumForm):
    # NOT WORKING - have to do this in the views.py
    # def __int__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.__disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    # NOT WORKING
    # def __disabled_fields(self):
    #     for field in self.fields.values():
    #         # field.widget.attrs['readonly'] = 'readonly'
    #         # field.widget.attrs['disabled'] = 'disabled`  # can try with: True
    #         field.required = False

    # TODO: I can do it only this way
    # class Meta:
    #     model = Album
    #     fields = '__all__'
    #     widgets = {
    #         'album_name': forms.TextInput(
    #             attrs={
    #                 'disabled': 'disabled',
    #             }
    #         ),
    #     }
