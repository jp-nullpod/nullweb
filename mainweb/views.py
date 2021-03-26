from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.http import HttpResponse
from django.utils import translation
from django.shortcuts import redirect

def change_language(request, lang):
    user_language = lang
    translation.activate(user_language)
    response = HttpResponse()
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return redirect(request.META['HTTP_REFERER'])

def index(request):
    return render(request, 'mainweb/home.html')

def projects(request):
    return render(request, 'mainweb/projects.html')

def about(request):
    return render(request, 'mainweb/about.html')
