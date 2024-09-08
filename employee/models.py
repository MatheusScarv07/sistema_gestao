from django.db import models

# Create your models here.
class Employee(models.Model):

   
    nome = models.CharField(max_length=70, null=True)
    cargo = models.CharField(max_length=70, null=True)
    status = models.BooleanField(null=True)

