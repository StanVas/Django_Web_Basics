# Generated by Django 4.2.2 on 2023-06-22 12:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
