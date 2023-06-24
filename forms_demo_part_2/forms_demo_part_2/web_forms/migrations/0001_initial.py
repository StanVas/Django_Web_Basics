# Generated by Django 4.2.2 on 2023-06-16 09:20

from django.db import migrations, models
import forms_demo_part_2.web_forms.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=30, validators=[forms_demo_part_2.web_forms.validators.validate_text])),
                ('priority', models.IntegerField(validators=[forms_demo_part_2.web_forms.validators.ValueInRangeValidator(1, 10)])),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]
