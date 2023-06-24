from django.http import HttpResponse
from django.shortcuts import render

from forms_demo_part_2.web_forms.forms import TodoForm, TodoCreateForm, PersonCreateForm
from forms_demo_part_2.web_forms.models import Person


def index(request):
    if request.method == 'GET':
        form = TodoForm()
    else:
        form = TodoForm(request.POST)

        if form.is_valid():
            return HttpResponse('All is valid')

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)


def todo_create(request):
    if request.method == 'GET':
        form = TodoCreateForm()
    else:
        form = TodoCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('All is valid')

    context = {
        'form': form,
    }

    return render(request, 'todo_create_form.html', context)


def list_persons(request):
    context = {
        'persons': Person.objects.all(),
    }

    return render(request, 'list-person.html', context)


def create_person(request):
    if request.method == 'GET':
        form = PersonCreateForm()
    else:
        form = PersonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
    }

    return render(request, 'create-person.html', context)
