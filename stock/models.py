from django.db import models
from supplier.models import Supplier

# Create your models here.
class Stock(models.Model):
    nome = models.TextField(max_lenght=255)
    descricao = models.TextField(max_lenght=70,null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.FloatField(null=True)
    categoria = models.TextField(null=True, blank=True)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_custo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade_minima_estoque = models.FloatField(null=True, blank=True)
    unidade_medida = models.TextField(null=True, blank=True)
    fornecedor = models.TextField(null=True, blank=True)
    fornecedor_id = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    localizacao_estoque = models.TextField(null=True, blank=True)
    status_produto = models.TextField(null=True, blank=True)
    garantia = models.TextField(null=True, blank=True)
    observacao_adicional = models.TextField(null=True, blank=True)
