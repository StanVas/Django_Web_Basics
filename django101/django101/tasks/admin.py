from django.contrib import admin

from django101.tasks.models import Task


# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # pass
    list_display = ('id', 'name', 'priority')
    # this shows what will be displayed in the admin panel
