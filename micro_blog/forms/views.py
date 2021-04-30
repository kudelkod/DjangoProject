from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from . import forms


# Create your views here.

def search_form(request):
    return render(request, 'search_form.html', {})


def search(request):
    if request.method == "GET":
        if 'q' in request.GET:
            return HttpResponse("Вы хотели найти %s" % request.GET['q'])
        else:
            return HttpResponse("Вы отправили пустую форму")


def test_view(request):
    return HttpResponse("Welcome to %s" % request.is_secure())


def file_input(request):
    name = request.POST['name']
    surname = request.POST['surname']
    gender = request.POST['gender']
    some_file = open('some.txt', 'w')
    some_file.write('Name: ' + name + '\n')
    some_file.write('Surname: ' + surname + '\n')
    some_file.write('Gender: ' + gender + '\n')
    some_file.close()
    return HttpResponse('Data is write')


def form(request):
    form_for_author = forms.AuthorForm
    form_for_article = forms.ArticleForm
    form_contact = forms.ContactForm
    context = {
        'form_for_author': form_for_author,
        'form_for_article': form_for_article,
        'form_contact': form_contact,
    }
    return render(request, 'form.html', context)


def author_add(request):
    form = forms.AuthorForm(request.POST)
    result = "Author %s added" % request.path
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            print(data)
            return HttpResponse("Author added! %s" % request.path)


def article_add(request):
    form = forms.ArticleForm(request.POST)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        form.save()
        return HttpResponse("Article added!")


class ContactFormView(generic.TemplateView):
    form_for_author = forms.AuthorForm
    form_for_article = forms.ArticleForm
    form_contact = forms.ContactForm

    def post(self, request):
        form = forms.ContactForm(request.POST)
        context = {
            'form_for_author': self.form_for_author,
            'form_for_article': self.form_for_article,
            'form_contact': form,
        }
        if form.is_valid():
            data = form.cleaned_data
            return HttpResponse(data.items())
        else:
            return render(request, 'form.html', context)

    def get(self, request):
        context = {
            'form_for_author': self.form_for_author,
            'form_for_article': self.form_for_article,
            'form_contact': self.form_contact,
        }
        return render(request, 'form.html', context)


class UrlView(generic.TemplateView):
    form_submit_url = forms.UrlForm

    def get(self, request):
        context = {
            'form_url': self.form_submit_url
        }
        return render(request, 'url_form.html', context)

    def post(self, request):
        form = forms.UrlForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            print(data)
        else:
            print('invalid')
            context = {
                'form_url': form
            }
            return render(request, 'url_form.html', context)
        return HttpResponse(form.cleaned_data.items())

