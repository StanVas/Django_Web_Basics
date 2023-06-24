from django.shortcuts import render, redirect

from online_library.web.forms import ProfileCreateForm, BookAddForm, BookEditForm, ProfileEditForm, ProfileDeleteForm
from online_library.web.models import Profile, Book


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    context = {
        'profile': profile,
        'books': Book.objects.all(),
    }

    return render(request, 'home/home-with-profile.html', context)


def book_details(request, pk):
    book = Book.objects.filter(pk=pk).get

    context = {
        'book': book,
    }

    return render(request, 'book/book-details.html', context)


def book_add(request):
    if request.method == 'GET':
        form = BookAddForm()
    else:
        form = BookAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'book/add-book.html', context)


def book_edit(request, pk):
    book = Book.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = BookEditForm(instance=book)
    else:
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'book': book,
    }

    return render(request, 'book/edit-book.html', context)


def book_delete(request, pk):
    book = Book.objects.filter(pk=pk).get()
    book.delete()
    return redirect('index')


def show_profile(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'profile/profile.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'home/home-no-profile.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    for field in form.fields.values():
        field.widget.attrs['disabled'] = 'disabled'
        # field.widget.attrs['disabled'] = True  # same as 'disabled'?

    context = {
        'form': form,
    }

    return render(request, 'profile/delete-profile.html', context)
