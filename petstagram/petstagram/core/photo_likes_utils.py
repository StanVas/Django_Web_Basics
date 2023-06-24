def apply_likes_count(photo):
    # we get photolike_set from common\models.py -> "class PhotoLike"
    photo.likes_count = photo.photolike_set.count()
    return photo


def apply_user_liked_photo(photo):
    # TODO: fix this for current user when we have authentication
    photo.is_liked_by_user = photo.likes_count > 0
    return photo
