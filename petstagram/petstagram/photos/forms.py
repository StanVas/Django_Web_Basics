from django import forms

from petstagram.common.models import PhotoComment
from petstagram.photos.models import Photo


class PhotoCommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                    'placeholder': 'Add comment...',
                },
            ),
        }


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('date_of_publication',)


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('date_of_publication', 'photo',)


class PhotoDeleteForm(PhotoBaseForm):
    pass
