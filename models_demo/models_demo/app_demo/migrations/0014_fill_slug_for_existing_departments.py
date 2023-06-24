# Generated by Django 4.2.1 on 2023-06-02 13:00

from django.db import migrations
from django.utils.text import slugify


def add_slug(apps, schema_editor):
    Department = apps.get_model("app_demo", "Departments")
    departments = Department.objects.all()

    for department in departments:
        department.slug = slugify(department.department_name)

    Department.objects.bulk_update(departments, ['slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('app_demo', '0013_alter_departments_options_departments_slug'),
    ]

    operations = [
        migrations.RunPython(add_slug),
    ]