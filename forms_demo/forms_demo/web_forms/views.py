from django import forms
from django.shortcuts import render

from forms_demo.web_forms.forms import NameForm
from forms_demo.web_forms.models import Person


def index(request):
    name = None

    if request.method == 'GET':
        form = NameForm()
    else:
        form = NameForm(request.POST)
        form.is_valid()
        # - validates the form, returns `True` or `False`
        # - fills `cleaned_data`

        name = form.cleaned_data['your_name']
        Person.objects.create(
            name=name,
        )

    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'index.html', context)


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # or fields = ('name', 'age', etc...)
        # exclude = ('pets', 'name', etc...)


def index_model_form(request):
    if request.method == 'GET':
        form = PersonModelForm()
    else:
        form = PersonModelForm(request.POST)
        if form.is_valid():
            pets = form.cleaned_data.pop('pets')
            person = Person.objects.create(
                **form.cleaned_data
            )

            person.pets.set(pets)
            person.save()

    context = {
        'form': form,
    }

    return render(request, 'model-form.html', context)
