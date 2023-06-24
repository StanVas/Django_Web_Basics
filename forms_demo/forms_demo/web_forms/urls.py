from django.urls import path

from forms_demo.web_forms.views import index, index_model_form

urlpatterns = (
    path('', index, name='index'),
    path('modelforms/', index_model_form, name='model form')
)
