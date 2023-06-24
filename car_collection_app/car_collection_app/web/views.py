from django.shortcuts import render, redirect

from car_collection_app.web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from car_collection_app.web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        context = {
            'hide_nav_links': True,
        }
        return render(request, 'core/index.html', context)

    return render(request, 'core/index.html')


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'hide_nav_links': True,
    }

    return render(request, 'profile/profile-create.html', context)


def profile_details(request):
    profile = get_profile()
    cars = Car.objects.all()
    total_price = 0

    for car in cars:
        total_price += car.price

    context = {
        'profile': profile,
        'total_price': total_price,
    }

    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profile/profile-delete.html', context)


def catalogue(request):
    context = {
        'cars': Car.objects.all(),
    }

    return render(request, 'core/catalogue.html', context)


def car_create(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'car/car-create.html', context)


def car_details(request, pk):
    car = Car.objects.filter(pk=pk).get()

    context = {
        'car': car,
    }

    return render(request, 'car/car-details.html', context)


def car_edit(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car/car-edit.html', context)


def car_delete(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    for field in form.fields.values():
        field.widget.attrs['disabled'] = 'disabled'

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car/car-delete.html', context)
