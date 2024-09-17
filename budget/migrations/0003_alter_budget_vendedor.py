# Generated by Django 5.1.1 on 2024-09-17 00:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_alter_budget_cpf_cnpj_cliente_and_more'),
        ('employee', '0002_alter_employee_cargo_alter_employee_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.employee'),
        ),
    ]
