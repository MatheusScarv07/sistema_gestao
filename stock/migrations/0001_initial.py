# Generated by Django 5.1 on 2024-09-07 19:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
                ('descricao', models.TextField(blank=True, null=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estoque', models.IntegerField()),
                ('categoria', models.TextField(blank=True, null=True)),
                ('valor_venda', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('valor_custo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantidade_minima_estoque', models.IntegerField(blank=True, null=True)),
                ('unidade_medida', models.TextField(blank=True, null=True)),
                ('fornecedor', models.TextField(blank=True, null=True)),
                ('localizacao_estoque', models.TextField(blank=True, null=True)),
                ('status_produto', models.TextField(blank=True, null=True)),
                ('garantia', models.TextField(blank=True, null=True)),
                ('observacao_adicional', models.TextField(blank=True, null=True)),
                ('fornecedor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.supplier')),
            ],
        ),
    ]