from django.db import models
from django.urls import reverse


class AuditInfoMix(models.Model):

    class Meta:
        # No table will be created in the DB
        # Can be inherited in other models
        abstract = True

    # this will be automatically set on creation
    created_on = models.DateTimeField(
        auto_now=True,
    )

    # this will auto set on each 'save'/'update'
    updated_on = models.DateTimeField(
        auto_now_add=True,
    )


class Departments(AuditInfoMix, models.Model):
    class Meta:
        # in the admin page it appears like "Departmentss"
        verbose_name_plural = 'Departments'

    department_name = models.CharField(
        max_length=20,
        unique=True,
    )

    slug = models.SlugField(
        unique=True,
        default='None'
    )

    def get_absolute_url(self):
        url = reverse('department details', kwargs={
            'pk': self.pk,
            'slug': self.slug,
        })
        return url

    def __str__(self):
        return f'ID: {self.pk} - Department: {self.department_name}'


class Projects(AuditInfoMix, models.Model):
    project_name = models.CharField(
        max_length=20
    )

    code_name = models.CharField(
        max_length=15, unique=True
    )

    dead_line = models.DateField()

    def __str__(self):
        return f'ID: {self.pk} - Project: {self.code_name}'


class Employee(AuditInfoMix, models.Model):
    # class Meta:
    #     ordering = ('-first_name', 'last_name', 'years_of_experience')

    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=40,
    )

    # One - to - Many
    department = models.ForeignKey(
        Departments,
        on_delete=models.RESTRICT,  # CASCADE
        default=1
    )

    birth_date = models.DateField()

    years_of_experience = models.PositiveIntegerField()

    level = models.CharField(
        max_length=30,
        default='trainee'
    )

    work_full_time = models.BooleanField(default=True)

    # Many - to - Many
    projects = models.ManyToManyField(Projects)

    email = models.EmailField(
        # Adds 'UNIQUE' constraint
        unique=True,
    )

    review = models.TextField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'ID: {self.pk} - Name: {self.full_name} - Department:{self.department}'
