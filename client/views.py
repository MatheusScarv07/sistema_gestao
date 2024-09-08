from django.shortcuts import render
from django.http import HttpResponse
from .controler.client_control import ControlClient

def home(request):
    clientes = ControlClient.get_all()
    print(clientes)
    return render(request, 'client/pages/home.html' )
