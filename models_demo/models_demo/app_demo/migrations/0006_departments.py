# Generated by Django 4.2.1 on 2023-06-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_demo', '0005_alter_employee_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=20)),
            ],
        ),
    ]
