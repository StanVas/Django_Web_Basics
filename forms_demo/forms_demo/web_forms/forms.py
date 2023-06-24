from django import forms


class NameForm(forms.Form):
    JOBS = (
        (1, 'waiter'),
        (1, 'bartender'),
        (1, 'cook'),
        (1, 'hostess'),
    )

    your_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            # this corresponds to HTML attributes (normally this is done in the front-end/ mostly used for `class`)
            attrs={
                'placeholder': 'Enter name',
                'class': 'form-control',
            }
        )
    )

    # by default in the html file it will be displayed like `age` - the name of the variable
    age = forms.IntegerField(
        label='Your age',  # with, label we can change how it will be displayed
        initial=18,  # will put initial value
        help_text='enter your age',
    )

    email = forms.EmailField(
        widget=forms.EmailInput(),  # by default
    )

    url = forms.URLField(
        widget=forms.URLInput(),  # by default
    )

    secret = forms.CharField(
        widget=forms.PasswordInput,  # by default
    )

    story = forms.CharField(  # by default `CharField` type='text'
        widget=forms.Textarea(),  # with `widget` we can change it to `Textarea`
    )

    job_as_select_list = forms.ChoiceField(
        choices=JOBS,
        widget=forms.Select,  # this is the default for `ChoiceField`
    )

    job_as_checkbox = forms.ChoiceField(
        choices=JOBS,
        widget=forms.CheckboxSelectMultiple,
    )

    job_as_radio_button = forms.ChoiceField(
        choices=JOBS,
        widget=forms.RadioSelect(),
    )
