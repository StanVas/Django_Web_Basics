from django import forms

from GamesPlay_App.games.models import Profile, Game


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']


class ProfileEditForm(BaseProfileForm):
    pass


class ProfileDeleteForm(BaseProfileForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ()

    def save(self, commit=True):
        if commit:
            Game.objects.all().delete()
            self.instance.delete()
        return self.instance


class BaseGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class GameCreateForm(BaseGameForm):
    pass


class GameEditForm(BaseGameForm):
    pass


class GameDeleteForm(BaseGameForm):
    def __init__(self, *args, **kwargs):

        # first call parent's constructor
        super(GameDeleteForm, self).__init__(*args, **kwargs)

        # there's a `fields` property now
        self.fields['title'].required = False
        self.fields['category'].required = False
        self.fields['rating'].required = False
        self.fields['max_level'].required = False
        self.fields['image_url'].required = False
        self.fields['summary'].required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
