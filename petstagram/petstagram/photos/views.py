from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoCommentForm
from petstagram.core.photo_likes_utils import apply_likes_count, apply_user_liked_photo
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from petstagram.photos.models import Photo


def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    likes = photo.photolike_set.all()

    apply_likes_count(photo)
    apply_user_liked_photo(photo)

    comments = photo.photocomment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': PhotoCommentForm,
    }

    return render(request, 'photos/photo-details-page.html', context)


def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()  # form.save() returns the object saved
            return redirect('details photo', pk=photo.pk)

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.filter(id=pk).get()

    if request.method == 'GET':
        form = PhotoEditForm(instance=photo)
    else:
        form = PhotoEditForm(request.POST, instance=photo, )
        if form.is_valid():
            form.save()
            return redirect('details photo', pk=pk)

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    # Like in the presentation
    photo = Photo.objects.filter(id=pk).get()
    photo.delete()

    return redirect('index')
