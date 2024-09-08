from django.db import models
from supplier.models import Supplier

# Create your models here.
class Stock(models.Model):
    nome = models.CharField(max_lenght=255)
    descricao = models.CharField(max_lenght=70,null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.FloatField(null=True)
    categoria = models.CharField(null=True, blank=True)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_custo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade_minima_estoque = models.FloatField(null=True, blank=True)
    unidade_medida = models.CharField(null=True, blank=True)
    fornecedor = models.CharField(null=True, blank=True)
    fornecedor_id = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    localizacao_estoque = models.CharField(null=True, blank=True)
    status_produto = models.CharField(null=True, blank=True)
    garantia = models.CharField(null=True, blank=True)
    observacao_adicional = models.CharField(null=True, blank=True)
