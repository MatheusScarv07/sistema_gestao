# Generated by Django 5.1.1 on 2024-10-21 22:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0004_alter_supplier_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='bairro',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='cep',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='cidade',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='cnpj',
            field=models.CharField(max_length=14, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contato',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='estado',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='nome',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='numero',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='rua',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
