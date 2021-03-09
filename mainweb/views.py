from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'mainweb/home.html')

def projects(request):
    return render(request, 'mainweb/projects.html')

def about(request):
    return render(request, 'mainweb/about.html')
