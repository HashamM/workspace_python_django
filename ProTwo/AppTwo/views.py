from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<em>My Second App HOME PAGE</em>")

def newPage(request):
    return HttpResponse("<h1> This is My NEW Page </h1>")

def help(request):
    my_help = {"help_me" : "This is Helper BOT from AppTwo"}
    return render(request, "AppTwo/helpPage.html", context=my_help)
