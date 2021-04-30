from django.shortcuts import render
from django.http import HttpResponse

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
    context = {
        'form_for_author': form_for_author,
        'form_for_article': form_for_article,
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

