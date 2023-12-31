# Generated by Django 4.2.1 on 2023-06-02 11:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_demo', '0011_employee_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='departments',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
