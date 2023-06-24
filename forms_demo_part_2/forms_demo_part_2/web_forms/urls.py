from django.conf.urls.static import static
from django.urls import path

from forms_demo_part_2 import settings
from forms_demo_part_2.web_forms.views import index, todo_create, list_persons, create_person

urlpatterns = [
    path('', index, name='index'),
    path('todo-create-form/', todo_create, name='todo create form'),
    path('persons/', list_persons, name='list persons'),
    path('person/create/', create_person, name='person create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
