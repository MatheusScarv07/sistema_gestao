# Generated by Django 5.0.13 on 2025-03-25 22:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('employee', '__first__'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartTemp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cliente', models.IntegerField(blank=True, null=True)),
                ('id_produto', models.IntegerField(blank=True, null=True)),
                ('name_product', models.CharField(max_length=70)),
                ('quantidade', models.FloatField(null=True)),
                ('valor_uni', models.FloatField(null=True)),
                ('valor_total', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_sale', models.IntegerField(null=True)),
                ('data_venda', models.DateField(auto_now_add=True)),
                ('cpf_cnpj_cliente', models.CharField(blank=True, max_length=14, null=True)),
                ('valor_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client')),
                ('produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.stock')),
                ('vendedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='SaleInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_sale', models.IntegerField(null=True)),
                ('data_venda', models.DateField(auto_now_add=True)),
                ('cpf_cnpj', models.CharField(max_length=14, null=True)),
                ('valor', models.FloatField(null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('vendedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
    ]
