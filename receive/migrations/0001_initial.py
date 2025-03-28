# Generated by Django 5.0.13 on 2025-03-25 22:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(null=True)),
                ('data_venda', models.DateField(auto_now_add=True)),
                ('cpf_cnpj', models.CharField(max_length=14, null=True)),
                ('status', models.CharField(max_length=14, null=True)),
                ('valor', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('data_venda', models.DateField(auto_now_add=True)),
                ('cpf_cnpj', models.CharField(max_length=14, null=True)),
                ('valor', models.FloatField(null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]
