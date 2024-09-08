from django.db import models

# Create your models here.

class Client(models.Model):
    nome = models.CharField(max_length=70, null=False )
    email = models.EmailField(unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=11, null=False )
    cpf_cnpj_cliente = models.CharField(max_length=14, null=False, unique=True)
    rg_cliente = models.CharField(max_length=15, null=True)
    inscricao_estadual_cliente = models.CharField(max_length=9, null=False)
    numero_casa = models.IntegerField(null=True)
    complemento = models.CharField(max_length=100, null=True)
    bairro = models.CharField(max_length=70, null=True)
    cidade = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
