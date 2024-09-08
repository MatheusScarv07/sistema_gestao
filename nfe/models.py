from django.db import models
from supplier.models import Supplier
from stock.models import Stock

# Create your models here.

class NFE(models.Model):
    fornecedor = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    data_entrada = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    nome_fornecedor = models.TextField(max_lenght=70,null=True, blank=True)
    cnpj = models.TextField(max_lenght=14,null=True, blank=True)
    data_emissao = models.DateTimeField(null=True, blank=True)
    numero_nota = models.TextField(null=True, blank=True)
    produto = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, blank=True)
    nome_produto = models.TextField(null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    