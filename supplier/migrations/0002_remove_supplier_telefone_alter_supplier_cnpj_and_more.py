# Generated by Django 5.1 on 2024-09-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='telefone',
        ),
        migrations.AlterField(
            model_name='supplier',
            name='cnpj',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contato',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='endereco',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='nome',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
