from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.forms import PhotoCommentForm, PhotoSearchForm
from petstagram.common.models import PhotoLike
from petstagram.core.photo_likes_utils import apply_likes_count, apply_user_liked_photo
from petstagram.photos.models import Photo


# def apply_likes_count(photo):
#                         # we get photolike_set from common\models.py -> "class PhotoLike"
#     photo.likes_count = photo.photolike_set.count()
#     return photo
#
#
# def apply_user_liked_photo(photo):
#     # TODO: fix this for current user when we have authentication
#     photo.is_liked_by_user = photo.likes_count > 0
#     return photo


def index(request):
    search_form = PhotoSearchForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['pet_name']

    # TODO fix this when auth
    photos = Photo.objects.all()

    if search_pattern:
        photos = photos.filter(tagged_pets__name__icontains=search_pattern)  # "icontains" = case insensitive

    # photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_likes_count(photo) for photo in photos]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    comment_form = PhotoCommentForm()

    context = {
        'photos': photos,
        'comment_form': comment_form,
        'search_form': search_form,
    }

    return render(request, 'common/home-page.html', context)


def get_user_liked_photos(photo_id):
    # TODO: fix when auth
    return PhotoLike.objects.filter(photo_id=photo_id)


def like_photo(request, photo_id):
    # Variant 1
    # photo_like = PhotoLike(
    #     photo_id=photo_id,
    # )
    # photo_like.save()

    user_liked_photos = get_user_liked_photos(photo_id)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        # Variant 2
        PhotoLike.objects.create(
            photo_id=photo_id,
        )

    # Variant 3 (wrong in this case - additional call to db)
    # Correct only if validation is needed
    # photo = Photo.objects.get(pk=photo_id)
    # Photo.objects.create(
    #     photo=photo,
    # )

    return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    # pyperclip.copy() ((from pyperclip import copy))
    copy(request.META['HTTP_HOST'] + resolve_url('details photo', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()

    form = PhotoCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)  # doesn't persist to DB, but we still get the obj
        comment.photo = photo
        comment.save()

    return redirect('index')
