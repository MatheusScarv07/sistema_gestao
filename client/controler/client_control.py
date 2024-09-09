from client.models import Client

class ControlClient:
    def register(self):
        # Implemente o método para registrar um cliente
        pass
    
    def get_all(self):
        try:
            clients = Client.objects.all().order_by('nome')
            clients_list = [self._model_to_dict(client) for client in clients]
            return clients_list
        except Exception as e:
            msg = f'Algo deu errado: {e}'
            return msg

    def get_by_id(self, client_id):
        try:
            # Busca o cliente pelo ID
            client = Client.objects.get(id=client_id)
            
            # Converte o cliente para um dicionário
            client_dict = self._model_to_dict(client)
            
            return client_dict
        except Client.DoesNotExist:
            # Retorna uma mensagem de erro caso o cliente não seja encontrado
            return f'Cliente com ID {client_id} não encontrado.'
        except Exception as e:
            # Captura outros erros e retorna a mensagem de erro
            msg = f'Algo deu errado: {e}'
            return msg

    def _model_to_dict(self, obj):
        """
        Converte um objeto de modelo Django para um dicionário.
        """
        return {field.name: getattr(obj, field.name) for field in obj._meta.fields}