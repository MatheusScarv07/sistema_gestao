from client.models import Client

def get_clients():
    controler_cliente = Client()
    clients = controler_cliente.objects.all()
    return clients
