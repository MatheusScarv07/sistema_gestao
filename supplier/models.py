from django.db import models

# Create your models here.
class Supplier(models.Model):
    nome = models.CharField(max_length=70, null=False)
    contato = models.CharField(max_length=11, null=False)
    endereco = models.CharField(max_length=255, null=False)
    cnpj = models.CharField(max_length=14, null=False)
    email = models.EmailField(null=True, blank=True)
