from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    nome = 'Cristian'
    return HttpResponse('OLÀ')
