# Generated by Django 5.1.1 on 2024-10-10 23:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0002_remove_supplier_telefone_alter_supplier_cnpj_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emissao', models.DateField(blank=True, null=True)),
                ('numero_nota', models.CharField(blank=True, max_length=20, null=True)),
                ('valor_boleto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('data_vencimento', models.DateField(blank=True, null=True)),
                ('data_entrada', models.DateField(auto_now_add=True)),
                ('fornecedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.supplier')),
            ],
        ),
    ]
