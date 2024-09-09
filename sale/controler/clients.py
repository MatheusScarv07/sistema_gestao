from client.controler.client_control import ControlClient


def get_clients():
    controler_cliente = ControlClient()
    clients = controler_cliente.get_all()
    return clients
