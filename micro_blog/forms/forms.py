from django.forms import ModelForm, Form
from django import forms
from .models import Author
from .models import Article
from django.http import HttpResponse


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = [field.name for field in model._meta.fields]


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = [field.name for field in model._meta.fields]
