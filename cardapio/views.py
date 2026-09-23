from django.db.models import Q
from django.shortcuts import render
from .models import Prato, Combo


def lista_pratos(request):
    """
    Listagem principal de pratos.

    Feature 1 (busca e filtro):
    - 'q' filtra por nome do prato (case-insensitive).
    - 'categoria' filtra por categoria (Entrada / Prato Principal /
      Sobremesa / Bebida).
    Os dois parametros podem ser usados juntos ou separadamente, e sao
    combinados com Q() numa unica consulta (desafio extra do enunciado).
    A listagem continua so mostrando pratos disponiveis (regra ja
    existente antes da feature).
    """
    termo_busca = request.GET.get('q', '').strip()
    categoria_selecionada = request.GET.get('categoria', '')

    filtros = Q(disponivel=True)

    if termo_busca:
        filtros &= Q(nome__icontains=termo_busca)

    if categoria_selecionada:
        filtros &= Q(categoria=categoria_selecionada)

    pratos = Prato.objects.filter(filtros).order_by('nome')

    contexto = {
        'pratos': pratos,
        'termo_busca': termo_busca,
        'categoria_selecionada': categoria_selecionada,
        'categorias': Prato.CATEGORIA_CHOICES,
    }
    return render(request, 'cardapio/pratos_list.html', contexto)


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