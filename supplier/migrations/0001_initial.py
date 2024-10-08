# Generated by Django 5.1 on 2024-09-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
                ('contato', models.TextField(blank=True, null=True)),
                ('endereco', models.TextField(blank=True, null=True)),
                ('cnpj', models.TextField(blank=True, null=True)),
                ('telefone', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
