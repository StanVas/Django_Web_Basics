from django.urls import path

from online_library.web.views import index, book_add, book_edit, book_details, show_profile, profile_edit, \
    profile_delete, book_delete

urlpatterns = (
    path('', index, name='index'),
    path('add/', book_add, name='book add'),
    path('edit/<int:pk>', book_edit, name='book edit'),
    path('details/<int:pk>', book_details, name='book details'),
    path('delete/<int:pk>', book_delete, name='book delete'),
    path('profile/', show_profile, name='show profile'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', profile_delete, name='profile delete'),
)
