from django.db import models
from client.models import Client
from supplier.models import Supplier
from stock.models import Stock
from employee.models import Employee

# Create your models here.
class Sale(models.Model):
    num_sale = models.IntegerField(null=True)
    cliente = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    data_venda = models.DateField(auto_now_add=True)
    vendedor = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    cpf_cnpj_cliente = models.CharField(max_length=14,null=True, blank=True)
    produto = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.cliente
    
class SaleInfo(models.Model):
    num_sale = models.IntegerField(null=True)
    data_venda = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    cpf_cnpj = models.CharField(max_length=14, null=True)
    vendedor = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True) 
    valor = models.FloatField(null=True)

class CartTemp(models.Model):
    id_cliente = models.IntegerField(null=True, blank=True)
    id_produto = models.IntegerField(null=True, blank=True)
    name_product = models.CharField(max_length=70)
    quantidade = models.FloatField(null=True)
    valor_uni = models.FloatField(null=True)
    valor_total = models.FloatField(null=True)

    def __str__(self):
        return self.name_product
    
