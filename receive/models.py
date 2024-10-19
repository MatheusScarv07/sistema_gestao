from django.db import models
from client.models import Client
from employee.models import Employee
from sale.models import SaleInfo
# Create your models here.

class PaymentType(models.Model):
    nome = models.CharField(max_length=20, null=True)


class Receive(models.Model):
    data = models.DateField(null=True)
    num_sale = models.ForeignKey(SaleInfo, on_delete=models.CASCADE)
    data_venda = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    cpf_cnpj = models.CharField(max_length=14, null=True)
    tipo_pagamento = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    status = models.CharField(max_length=14, null=True)
    valor = models.FloatField(null=True)

class PaymentHistory(models.Model):
    data = models.DateField(auto_now_add=True)
    num_sale = models.ForeignKey(SaleInfo, on_delete=models.CASCADE)
    data_venda = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    cpf_cnpj = models.CharField(max_length=14, null=True)
    type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    valor = models.FloatField(null=True)


