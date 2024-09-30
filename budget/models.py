from django.db import models
from client.models import Client
from employee.models import Employee
from stock.models import Stock

# Create your models here.
class Budget(models.Model):
    number_budget = models.IntegerField(null=True)
    cliente = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    data_orcamento = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cpf_cnpj_cliente = models.CharField(max_length=14,null=True, blank=True)
    nome_cliente = models.CharField(max_length=70, null=True )
    vendedor = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    produto = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)




class BudgetInfo(models.Model):
    number_budget = models.IntegerField(null=True)
    data_orcamento = models.DateField(auto_now_add=True)
    cpf_cnpj_cliente = models.CharField(max_length=14,null=True, blank=True)
    cliente = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    vendedor = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

   
class CartTempBudget(models.Model):
    id_cliente = models.IntegerField(null=True, blank=True)
    id_produto = models.IntegerField(null=True, blank=True)
    name_product = models.CharField(max_length=70)
    quantidade = models.FloatField(null=True)
    valor_uni = models.FloatField(null=True)
    valor_total = models.FloatField(null=True)

    def __str__(self):
        return self.name_product
