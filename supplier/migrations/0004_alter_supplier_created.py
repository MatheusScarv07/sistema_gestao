# Generated by Django 5.1 on 2024-10-09 22:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0003_rename_endereco_supplier_rua_supplier_bairro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='created',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
