from django.shortcuts import render

from .models import Categoria
from .models import Anuncio


def home(request):
    categorias = Categoria.objects.all()
    anuncios = Anuncio.objects.all()[:9]

    return render(request, 'home.html', {'categorias': categorias,
                                         'anuncios': anuncios})
