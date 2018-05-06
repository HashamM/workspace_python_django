from django.conf.urls import url
from django.urls import path
from AppTwo import views

urlpatterns = [
    path('', views.home, name="home"),
    path('new_page/', views.newPage, name="newPage"),
    path('help/', views.help, name="helpPage")
]
