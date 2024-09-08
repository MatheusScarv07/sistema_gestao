from django.db import models

# Create your models here.

class Client(models.Model):
    nome = models.CharField(max_length=70, null=False )
    email = models.EmailField(unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=11, null=False )
    endereco = models.CharField(max_length=255, null=False )
    nome_fantasia = models.CharField(max_length=70, null=False)
    cpf_cnpj_cliente = models.CharField(max_length=14, null=False, unique=True)
    rg_cliente = models.TextField(null=True, blank=True)
    inscricao_estadual_cliente = models.TextField(null=True, blank=True)
    telefone_contato = models.TextField(null=True, blank=True)
    telefone_celular = models.TextField(null=True, blank=True)
    numero_casa = models.TextField(null=True, blank=True)
    complemento = models.TextField(null=True, blank=True)
    bairro = models.TextField(null=True, blank=True)
    cidade = models.TextField(null=True, blank=True)
    estado = models.TextField(null=True, blank=True)
    created_at = models.DateField()
