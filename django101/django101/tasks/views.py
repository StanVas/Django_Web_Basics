import http.client
from django import http

from django.shortcuts import render

from django101.tasks.models import Task


# Create your views here.


def simple_example(request):
    return http.HttpResponse('It works')


def get_all_tasks(request):
    # .order_by('id') is just an option we can add
    all_tasks = Task.objects.order_by('id').all()
    # [name(id), name(id)]
    result = ', '.join(f'{t.name}({t.id})' for t in all_tasks)

    if not result:
        result = "There are no created tasks!"

    return http.HttpResponse(result)


def index(request):
    all_tasks = Task.objects.order_by('id').all()
    context = {
        'title': 'The tasks app!',
        'tasks': all_tasks,
    }

    return render(request, 'index.html', context)
