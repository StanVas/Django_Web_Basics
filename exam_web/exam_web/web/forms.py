from django import forms

from exam_web.web.models import Profile, Fruit


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""

    class Meta:
        model = Profile
        exclude = ['image_url', 'age']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'placeholder': 'Password',
                }
            ),
        }


class ProfileEditForm(BaseProfileForm):
    class Meta:
        model = Profile
        exclude = ['email', 'password']


class ProfileDeleteForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            Fruit.objects.all().delete()
            self.instance.delete()
        return self.instance


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class FruitCreateForm(BaseFruitForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""

    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description',
                }
            ),
            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info',
                }
            ),
        }


class FruitEditForm(BaseFruitForm):
    pass


class FruitDeleteForm(BaseFruitForm):
    def __init__(self, *args, **kwargs):
        super(FruitDeleteForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['image_url'].required = False
        self.fields['description'].required = False

    class Meta:
        model = Fruit
        exclude = ['nutrition']

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
