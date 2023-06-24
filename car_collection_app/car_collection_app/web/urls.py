from django.urls import path, include

from car_collection_app.web.views import index, profile_create, profile_details, profile_edit, profile_delete, \
    catalogue, car_create, car_details, car_delete, car_edit

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
    path('car/', include([
        path('create/', car_create, name='car create'),
        path('<int:pk>/details/', car_details, name='car details'),
        path('<int:pk>/edit/', car_edit, name='car edit'),
        path('<int:pk>/delete/', car_delete, name='car delete'),
    ]))
)


# http://localhost:8000/car/create/ - car create page
# http://localhost:8000/car/<car-id>/details/ - car details page
# http://localhost:8000/car/<car-id>/edit/ - car edit page
# http://localhost:8000/car/<car-id>/delete/ - car delete page
