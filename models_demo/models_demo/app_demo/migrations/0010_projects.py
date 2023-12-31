# Generated by Django 4.2.1 on 2023-06-01 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_demo', '0009_alter_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=20)),
                ('code_name', models.CharField(max_length=15, unique=True)),
                ('dead_line', models.DateField()),
            ],
        ),
    ]
