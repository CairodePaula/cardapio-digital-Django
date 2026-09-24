from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Prato, Combo
from .forms import PratoForm


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


def cadastrar_prato(request):
    """
    Cadastro de prato via formulario no site (antes so existia pelo
    Django Admin). E aqui que a Feature 2 (validacao customizada do
    preco) e exercitada: se o preco for <= 0, o form volta com o erro
    e o template mostra a mensagem automaticamente via {{ form.as_p }}.
    """
    if request.method == 'POST':
        form = PratoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Prato cadastrado com sucesso.')
            return redirect('cardapio:lista_pratos')
    else:
        form = PratoForm()

    return render(request, 'cardapio/prato_form.html', {'form': form})
