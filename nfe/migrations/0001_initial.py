# Generated by Django 5.1 on 2024-09-07 19:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NFE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nome_fornecedor', models.TextField(blank=True, null=True)),
                ('cnpj', models.TextField(blank=True, null=True)),
                ('data_emissao', models.DateTimeField(blank=True, null=True)),
                ('numero_nota', models.TextField(blank=True, null=True)),
                ('nome_produto', models.TextField(blank=True, null=True)),
                ('valor_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fornecedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.supplier')),
                ('produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.stock')),
            ],
        ),
    ]
