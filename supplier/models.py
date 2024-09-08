from django.db import models

# Create your models here.
class Supplier(models.Model):
    nome = models.CharField(max_length=70, null=True)
    contato = models.CharField(max_length=11, null=True)
    endereco = models.CharField(max_length=255, null=True)
    cnpj = models.CharField(max_length=14, null=True)
    email = models.EmailField(null=True, blank=True)
