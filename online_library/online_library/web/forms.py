from django import forms

from online_library.web.models import Profile, Book


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(BaseProfileForm):
    pass


class ProfileEditForm(BaseProfileForm):
    pass


class ProfileDeleteForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(ProfileDeleteForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['image'].required = False

    def save(self, commit=True):
        if commit:
            Book.objects.all().delete()
            self.instance.delete()
        return self.instance


class BaseBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BookAddForm(BaseBookForm):
    pass


class BookEditForm(BaseBookForm):
    pass



