from django.core.validators import URLValidator
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


class ContactForm(forms.Form):
    boolean_field = forms.NullBooleanField()
    float_field = forms.FloatField()
    name_sender = forms.CharField(max_length=100, label="Enter your name")
    message = forms.CharField(widget=forms.Textarea, label="Message")
    sender = forms.EmailField(label="Enter your E-Mail")


def validate_url(value):
    validation_url = URLValidator()
    value_one_invalid = False
    value_two_invalid = False
    try:
        validation_url(value)
    except:
        value_one_invalid = True

    value_two_url = 'http://' + value
    try:
        validation_url(value_two_url)
    except:
        value_two_invalid = True

    if value_one_invalid == False and value_two_invalid == False:
        raise forms.ValidationError("Bad site URL")
    return value


def check_dot_com(value):
    if not'.com' in value:
        raise forms.ValidationError("It's not site URL")


class UrlForm(forms.Form):
    title = forms.CharField(label='Site name')
    url = forms.CharField(label='Site URL', validators=[validate_url, check_dot_com])

    # def clean(self):
    #     cleaned_data = super(UrlForm, self).clean()
    #
    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     validation_url = URLValidator()
    #     try:
    #         validation_url(url)
    #     except:
    #         raise forms.ValidationError("It's not site URL!")
    #     return url
