# Generated by Django 2.1.1 on 2018-10-03 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20181003_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='produtos',
            field=models.ManyToManyField(blank=True, to='clientes.Produto'),
        ),
    ]
