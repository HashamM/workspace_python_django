from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("HOME Page - Hello World!!")

def index(request):
    # below key:value will be called in template page linked
    my_dict = {'insert_me':"Hello I am from first_app/index.html !"}
    # render(request, template we want to use i.e file name, link_up to template file selected.)
    return render(request, 'first_app/index.html', context=my_dict)
