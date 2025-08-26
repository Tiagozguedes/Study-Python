from django.shortcuts import render
from django.http import HttpResponse

#Aqui tem tudo que vai ser visto em nosso App

def index(request):
    return HttpResponse('<h1>Hellow Word</h1>')