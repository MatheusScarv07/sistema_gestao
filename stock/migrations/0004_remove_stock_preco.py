# Generated by Django 5.1.1 on 2024-09-30 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_alter_stock_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='preco',
        ),
    ]