# Generated by Django 3.1 on 2020-09-01 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=200)),
                ('Cpf', models.CharField(max_length=14, unique=True)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Indicacao', models.TextField()),
                ('Status', models.CharField(choices=[('fazendo', 'Fazendo'), ('feito', 'Feito')], max_length=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]