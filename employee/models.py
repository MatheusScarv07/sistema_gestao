from django.db import models

# Create your models here.
class Employee(models.Model):

   
    nome = models.CharField(max_length=70, null=False)
    cargo = models.CharField(max_length=70, null=False)
    status = models.BooleanField(null=False)

