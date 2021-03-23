from django.db import models


class Categoria(models.Model):
    titulo = models.CharField(max_length=40)


    def __str__(self):
        return self.titulo


class Anuncio(models.Model):
    titulo = models.CharField(max_length=40)
    preco = models.DecimalField(max_digits=11, decimal_places=2)