# Generated by Django 5.0.13 on 2025-03-25 22:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('receive', '0001_initial'),
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenthistory',
            name='num_sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.saleinfo'),
        ),
        migrations.AddField(
            model_name='paymenthistory',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receive.paymenttype'),
        ),
        migrations.AddField(
            model_name='receive',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client'),
        ),
        migrations.AddField(
            model_name='receive',
            name='num_sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.saleinfo'),
        ),
        migrations.AddField(
            model_name='receive',
            name='tipo_pagamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receive.paymenttype'),
        ),
    ]
