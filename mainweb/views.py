from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.http import HttpResponse
from django.utils import translation
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

def change_language(request, lang):
    translation.activate(lang)
    response = HttpResponse()
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    return render(request, 'mainweb/home.html')
    
def index(request):
    return render(request, 'mainweb/home.html')

def projects(request):
    return render(request, 'mainweb/projects.html')

def about(request):
    return render(request, 'mainweb/about.html')
