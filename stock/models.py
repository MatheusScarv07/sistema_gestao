from django.db import models
from supplier.models import Supplier

# Create your models here.
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70,null=True)
    descricao = models.CharField(max_length=70,null=True, blank=True)
    estoque = models.FloatField(null=True)
    categoria = models.CharField(max_length=70,null=True, blank=True)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_custo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade_minima_estoque = models.FloatField(null=True, blank=True)
    unidade_medida = models.CharField(max_length=2,null=True, blank=True)
    fornecedor = models.CharField(max_length=70,null=True, blank=True)
    fornecedor_id = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    localizacao_estoque = models.CharField(max_length=70,null=True, blank=True)
    status_produto = models.BooleanField(default=True)
    garantia = models.CharField(max_length=20,null=True, blank=True)
    observacao_adicional = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.nome
    
