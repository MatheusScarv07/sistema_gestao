from django.db import models

# Create your models here.
class Supplier(models.Model):
    nome = models.TextField()
    contato = models.TextField(null=True, blank=True)
    endereco = models.TextField(null=True, blank=True)
    cnpj = models.TextField(null=True, blank=True)
    telefone = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
