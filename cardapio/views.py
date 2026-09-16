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


def buscar_pratos(request):
    """
    Busca de pratos por nome (texto livre), tipo e categoria.
    Os tres filtros sao opcionais e combinaveis (GET ?nome=&tipo=&categoria=).
    """
    nome = request.GET.get('nome', '').strip()
    tipo = request.GET.get('tipo', '')
    categoria = request.GET.get('categoria', '')

    pratos = Prato.objects.filter(disponivel=True)
    if nome:
        pratos = pratos.filter(nome__icontains=nome)
    if tipo:
        pratos = pratos.filter(tipo=tipo)
    if categoria:
        pratos = pratos.filter(categoria=categoria)

    contexto = {
        'pratos': pratos,
        'tipos': Prato.TIPO_CHOICES,
        'categorias': Prato.CATEGORIA_CHOICES,
        'filtros': {'nome': nome, 'tipo': tipo, 'categoria': categoria},
    }
    return render(request, 'cardapio/buscar_pratos.html', contexto)
