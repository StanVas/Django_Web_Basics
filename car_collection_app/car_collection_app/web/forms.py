from django import forms

from car_collection_app.web.models import Profile, Car


class ProfileBaseFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseFrom):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']


class ProfileEditForm(ProfileBaseFrom):
    pass


class ProfileDeleteForm(ProfileBaseFrom):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()
        return self.instance


class CarBaseFrom(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarCreateForm(CarBaseFrom):
    pass


class CarEditForm(CarBaseFrom):
    pass


class CarDeleteForm(CarBaseFrom):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(CarDeleteForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['type'].required = False
        self.fields['model'].required = False
        self.fields['year'].required = False
        self.fields['image_url'].required = False
        self.fields['price'].required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
