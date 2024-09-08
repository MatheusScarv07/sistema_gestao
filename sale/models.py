from django.db import models
from client.models import Client
from supplier.models import Supplier
from stock.models import Stock

# Create your models here.
class Sale(models.Model):
    cliente = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    data_venda = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cpf_cnpj_cliente = models.CharField(max_lenght=14,null=True, blank=True)
    nome_cliente = models.CharField(max_lenght=70,null=True, blank=True)
    vendedor = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    produto = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)