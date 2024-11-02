from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'nome', 'email', 'telefone', 'cpf_cnpj', 'rg',
            'rua', 'numero_casa', 'complemento', 'cep',
            'bairro', 'cidade', 'estado'
        ]