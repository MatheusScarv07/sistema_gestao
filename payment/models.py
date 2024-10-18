from django.db import models

class Payment(models.Model):
    num_nota = models.CharField(max_length=50)
    nome = models.CharField(max_length=70)
    cnpj = models.CharField(max_length=14)
    vencimento = models.DateField()
    data_venda = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):  
        return self.nome
