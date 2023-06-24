from django.shortcuts import render, redirect

from my_music_app.web.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
from my_music_app.web.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        # return redirect('add profile')
        return add_profile(request)

    context = {
        'albums': Album.objects.all(),
    }

    return render(request, 'core/home-with-profile.html', context)


def add_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'hide_nav_links': True,
    }

    return render(request, 'core/home-no-profile.html', context)


def details_profile(request):
    profile = get_profile()
    albums_count = Album.objects.count()

    context = {
        'profile': profile,
        'albums_count': albums_count,
    }

    return render(request, 'profiles/profile-details.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    # TODO: can't do it in the form. Have to be done here for now!
    for field in form.fields.values():
        field.widget.attrs['readonly'] = 'readonly'

    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-delete.html', context)


def details_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    context = {
        'album': album,
    }

    return render(request, 'albums/album-details.html', context)


def add_album(request):
    if request.method == 'GET':
        form = CreateAlbumForm()
    else:
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'albums/add-album.html', context)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'albums/edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteAlbumForm(instance=album)
    else:
        # Album.objects.filter(pk=pk).delete() # DON'T do this! Do it in the form(with save())!
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    # # TODO: can't do it in the form. Have to be done here for now!
    for field in form.fields.values():
        field.widget.attrs['readonly'] = 'readonly'
        # field.widget.attrs['disabled'] = 'disabled'  # problem with deleting in the form(says this field is required)

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'albums/delete-album.html', context)
