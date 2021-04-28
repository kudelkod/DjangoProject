from django.urls import path, re_path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.home),
    path('index', views.index),
    path('about', TemplateView.as_view(template_name='about.html', extra_context={'header': 'About this page'})),
    path('contact', TemplateView.as_view(template_name='contact.html')),
    path('base', TemplateView.as_view(template_name='base.html'))
]
