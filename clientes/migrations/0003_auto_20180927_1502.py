# Generated by Django 2.1.1 on 2018-09-27 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_person_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='clients_photos'),
        ),
    ]