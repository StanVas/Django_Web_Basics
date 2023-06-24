# Generated by Django 4.2.2 on 2023-06-24 08:40

import django.core.validators
from django.db import migrations, models
import exam_web.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_fruit_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), exam_web.web.validators.start_with_letter], verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(1), exam_web.web.validators.start_with_letter], verbose_name='Last Name'),
        ),
    ]
