# Generated by Django 3.2.7 on 2021-09-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0004_anuncio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='titulo',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
