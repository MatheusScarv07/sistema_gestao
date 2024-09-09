from django.shortcuts import render
from django.http import HttpResponse
from .controler.client_control import ControlClient

control_client = ControlClient()

def home(request):
      # Crie uma instância da classe ControlClient
    clients = control_client.get_all()  # Chame o método get_all da instância
    print(clients)
    return render(request, 'client/pages/home.html', context={
        'clientes':clients
    } )

def details_client(request, id):
    data = control_client.get_by_id(id)
    print(data)
    return render(request, 'client/pages/details_client.html', context={
        'client': data
    })

def register(request):
    return render(request, 'client/pages/register.html')