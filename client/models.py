from django.db import models
from django.utils import timezone
# Create your models here.

class Client(models.Model):
    nome = models.CharField(max_length=70, null=True )
    email = models.EmailField(unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=11, null=True )
    cpf_cnpj_cliente = models.CharField(max_length=14, null=True, unique=True)
    rg_cliente = models.CharField(max_length=15, null=True)
    inscricao_estadual_cliente = models.CharField(max_length=9, null=True)
    numero_casa = models.IntegerField(null=True)
    complemento = models.CharField(max_length=100, null=True)
    bairro = models.CharField(max_length=70, null=True)
    cidade = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=2, null=True)
    models.DateTimeField(default=timezone.now)
