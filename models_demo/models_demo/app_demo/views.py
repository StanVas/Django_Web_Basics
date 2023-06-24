from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from models_demo.app_demo.models import Employee, Departments


def index(request):
    context = {
        'employees': Employee.objects.all().order_by('first_name'),
        'department': Departments.objects.get(pk=1),
    }

    return render(request, 'index.html', context)


def department_details(request, pk, slug):
    context = {
        'department': get_object_or_404(Departments, pk=pk, slug=slug)
    }

    return render(request, 'department_details.html', context)


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()

    return redirect('index')
