from django.db import models
from datetime import datetime
from django.utils.timezone import now
# Create your models here.


class Supplier(models.Model):
    nome = models.CharField(max_length=70, null=False)  # Campo obrigatório
    cnpj = models.CharField(max_length=14, unique=True, null=False)  # CNPJ único e obrigatório
    email = models.EmailField(null=True, blank=True)
    contato = models.CharField(max_length=11, null=True, blank=True)
    rua = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=30, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    cep = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateField(default=now)  # Usar timezone.now() para garantir a data correta no momento da criação

    def __str__(self):
        return f'{self.nome} - CNPJ: {self.cnpj}'
