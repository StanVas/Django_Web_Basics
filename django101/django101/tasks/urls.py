from django.urls import path

from django101.tasks.views import simple_example, get_all_tasks, index

urlpatterns = (
    # http://localhost:8000/tasks/
    path('', index),
    # http://localhost:8000/tasks/example/
    path('example/', simple_example),
    # http://localhost:8000/tasks/all/
    path('all/', get_all_tasks),
)
