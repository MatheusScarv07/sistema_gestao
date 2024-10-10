from django.db import models
from datetime import datetime
# Create your models here.
class Supplier(models.Model):
    nome = models.CharField(max_length=70, null=True)
    cnpj = models.CharField(max_length=14, null=True)
    email = models.EmailField(null=True, blank=True)
    contato = models.CharField(max_length=11, null=True)
    rua = models.CharField(max_length=255, null=True)
    numero = models.CharField(max_length=10, null=True)
    bairro = models.CharField(max_length=50, null=True)
    cidade = models.CharField(max_length=30, null=True)
    estado = models.CharField(max_length=2, null=True)
    cep = models.CharField(max_length=20, null=True)
    created = models.DateField(default=datetime.today)
    
    

    def __str__(self):
        return self.nome
    
