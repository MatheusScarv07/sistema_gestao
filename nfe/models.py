from django.db import models
from supplier.models import Supplier
from stock.models import Stock

# Create your models here.

class NFE(models.Model):
    fornecedor = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    data_emissao = models.DateField(null=True, blank=True)
    numero_nota = models.CharField(max_length=20,null=True, blank=True)
    produto = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_entrada = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.produto.nome
    


class NFEInfo(models.Model):
    fornecedor = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    data_entrada = models.DateTimeField(auto_now_add=True)
    data_emissao = models.DateTimeField(null=True, blank=True)
    numero_nota = models.CharField(max_length=20,null=True, blank=True)
    quantidade_itens = models.IntegerField(null=True, blank=True)
    boleto = models.CharField(max_length=3, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        self.num = str(self.numero_nota)
        return self.num
    


class NFECartTemp(models.Model):
    fonecedor = models.IntegerField(null=True, blank=True)
    id_produto = models.IntegerField(null=True, blank=True)
    name_product = models.CharField(max_length=70)
    quantidade = models.FloatField(null=True)
    valor_uni = models.FloatField(null=True)
    valor_total = models.FloatField(null=True)

    def __str__(self):
        return self.name_product
    