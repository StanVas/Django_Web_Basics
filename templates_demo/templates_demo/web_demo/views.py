import random
from datetime import datetime

from django.shortcuts import render, redirect


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'Name: {self.name} --- Age: {self.age} years old'


def index(request):  # first we create a view then a template
    context = {
        'title': 'My Title',
        'value': random.random(),
        'info': {
            'address': 'Sofia',
            'age': 21,
        },
        'new_student': Student('Ivan', 19),
        'new_student_info': Student('Pesho', 21).get_info(),
        'now': datetime.now(),
        'students': ['Pesho', 'Ivan', 'Gosho', 'Maria', 'Stamat'],
        'custom_filter_test': list(range(20)),
    }

    return render(request, 'index.html', context)  # we connect the view with the template and add it to the app's urls


def redirect_to_home(request):
    return redirect('index')


def about(request):
    return render(request, 'about.html')