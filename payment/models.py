from django.db import models
from supplier.models import Supplier

# Create your models here.




class pay(models.Model):
    fornecedor = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    data_emissao = models.DateField(null=True, blank=True)
    numero_nota = models.CharField(max_length=20,null=True, blank=True)
    valor_boleto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_vencimento = models.DateField(null=True, blank=True)
    data_entrada = models.DateField(auto_now_add=True)
    
    
    

    def __str__(self):
        return self.produto.nome
    