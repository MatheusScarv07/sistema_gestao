# Generated by Django 5.1 on 2024-09-17 23:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_rename_cpf_cnpj_cliente_client_cpf_cnpj_and_more'),
        ('sale', '0005_alter_sale_vendedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='data_venda',
            field=models.DateField(auto_now_add=True),
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
            ],
        ),
    ]
