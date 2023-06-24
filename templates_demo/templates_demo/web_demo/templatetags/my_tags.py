from django.template import Library

from templates_demo.web_demo.views import Student

register = Library()


@register.simple_tag(name='student_info_custom_tag')
def show_student_info(student: Student):
    return f'Hello, my name is {student.name} and I am {student.age} years old!'


@register.inclusion_tag('inclusion_tags/nav.html', name='app_nav')
def generate_nav(*args):
    context = {
        'url_names': args
    }

    return context
