from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {"n": []}
    return render(request, "index.html", context)


def home(request):
    return HttpResponse("<h1>Home page</h1>")
