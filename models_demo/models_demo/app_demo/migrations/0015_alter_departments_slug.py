# Generated by Django 4.2.1 on 2023-06-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_demo', '0014_fill_slug_for_existing_departments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='slug',
            field=models.SlugField(default='None', unique=True),
        ),
    ]
