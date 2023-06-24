from django.urls import path, include

from my_music_app.web.views import index, details_profile, delete_profile, details_album, delete_album, edit_album, \
    add_album, add_profile

urlpatterns = (
    path('', index, name='index'),
    path('profile/', include([
        # path('add/', add_profile, name='add profile'),
        path('details/', details_profile, name='details profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
    path('album/', include([
        path('add/', add_album, name='add album'),
        path('details/<int:pk>/', details_album, name='details album'),
        path('edit/<int:pk>/', edit_album, name='edit album'),
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ])),
)

