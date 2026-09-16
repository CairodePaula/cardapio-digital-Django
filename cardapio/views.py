from django.shortcuts import render
from .models import Prato, Combo


def lista_pratos(request):
    # .filter(disponivel=True) usa o ORM para trazer do banco
    # somente os pratos marcados como disponiveis.
    pratos = Prato.objects.filter(disponivel=True)
    return render(request, 'cardapio/pratos_list.html', {'pratos': pratos})


def lista_combos(request):
    combos = Combo.objects.filter(disponivel=True).prefetch_related('pratos')
    # prefetch_related evita que o Django faca uma consulta extra ao banco
    # para cada combo, quando formos listar os pratos de cada um no template.
    return render(request, 'cardapio/combos_list.html', {'combos': combos})
