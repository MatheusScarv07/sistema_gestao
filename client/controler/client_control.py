from client.models import Client


class ControlClient():

    def register(self):
        ...
    def get_all():
        try:
            clients = Client.objects.all().order_by('nome')
            return clients
        except Exception as e:
            msg = f'Algo deu errado: {e}'
            return msg
    def get_by_id(self):
        ...

