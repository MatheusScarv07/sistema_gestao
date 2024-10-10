from client.models import Client

class ControlClient:
    def register(self):
        # Implemente o método para registrar um cliente
        pass
    
    def get_all():
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
    
    def get_estados(self):
        estados =[
            ('ac', 'Acre'),
            ('al', 'Alagoas'),
            ('ap', 'Amapá'),
            ('am', 'Amazonas'),
            ('ba', 'Bahia'),
            ('ce', 'Ceará'),
            ('df', 'Distrito Federal'),
            ('es', 'Espírito Santo'),
            ('go', 'Goiás'),
            ('ma', 'Maranhão'),
            ('mt', 'Mato Grosso'),
            ('ms', 'Mato Grosso do Sul'),
            ('mg', 'Minas Gerais'),
            ('pa', 'Pará'),
            ('pb', 'Paraíba'),
            ('pr', 'Paraná'),
            ('pe', 'Pernambuco'),
            ('pi', 'Piauí'),
            ('rj', 'Rio de Janeiro'),
            ('rn', 'Rio Grande do Norte'),
            ('rs', 'Rio Grande do Sul'),
            ('ro', 'Rondônia'),
            ('rr', 'Roraima'),
            ('sc', 'Santa Catarina'),
            ('sp', 'São Paulo'),
            ('se', 'Sergipe'),
            ('to', 'Tocantins')
]
        return estados