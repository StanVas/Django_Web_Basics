from django import forms
from django.core.exceptions import ValidationError

from forms_demo_part_2.web_forms.models import Todo, Person
from forms_demo_part_2.web_forms.validators import ValueInRangeValidator, validate_text


class TodoForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        validators=(
            validate_text,
        ),
        error_messages={
            'required': 'Todo text must be set!'
        },
    )
    priority = forms.IntegerField(
        validators=(
            # validate_priority,
            # MinValueValidator(1),  # build in validators from Django
            # MaxValueValidator(10),
            ValueInRangeValidator(1, 10),
        ),
    )
    is_done = forms.BooleanField(
        required=False,
    )

    # we can use `clean` methods for validations, but it's better to do validations
    # outside the form li ke in our case in the validators.py file with functions
    # def clean_text(self):
    #     pass
    #
    # def clean_priority(self):
    #     pass
    #
    # def clean_is_done(self):
    #     pass


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

    def clean(self):
        return super().clean()

    # def clean_text(self):
    #     """
    #     used for:
    #     1. Transform data into desired format/form
    #     2. Validations
    #     """
    #     return self.cleaned_data['text'].upper()

    def clean_assignee(self):
        assignee = self.cleaned_data['assignee']
        if assignee.todo_set.count() > Todo.MAX_TODOS_PER_PERSON:
            raise ValidationError(f'{assignee} already has max todos assigned')
        return assignee


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
