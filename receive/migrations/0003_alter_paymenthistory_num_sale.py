# Generated by Django 5.1 on 2024-10-18 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receive', '0002_receive_data'),
        ('sale', '0007_saleinfo_vendedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenthistory',
            name='num_sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.saleinfo'),
        ),
    ]
