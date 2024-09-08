from django.db import models

# Create your models here.
class Employee(models.Model):
    nome = models.TextField()
    cargo = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
