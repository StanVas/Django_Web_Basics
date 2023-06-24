from django.contrib import admin

from models_demo.app_demo.models import Employee, Departments, Projects


# the 'employee' model is enabled in django admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    # options in Django Admin
    list_display = ('pk', 'first_name', 'last_name', 'department', 'level',)
    list_filter = ('department',)
    search_fields = ('first_name',)


@admin.register(Departments)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    pass
