# Generated by Django 5.1 on 2024-09-16 23:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_cargo_alter_employee_nome_and_more'),
        ('sale', '0004_remove_sale_nome_cliente_remove_sale_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.employee'),
        ),
    ]
