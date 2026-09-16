from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from restaurante.models import Mesa
from .models import Comanda, ItemComanda
from .forms import AdicionarPratoForm, AdicionarComboForm, AlterarQuantidadeForm


def abrir_comanda(request, mesa_id):
    """
    Abre uma comanda nova para a mesa informada.
    """
    mesa = get_object_or_404(Mesa, pk=mesa_id)
    comanda = Comanda.objects.create(mesa=mesa)

    messages.success(request, f'Comanda aberta para a {mesa}.')
    return redirect('comandas:detalhe_comanda', comanda_id=comanda.pk)


def detalhe_comanda(request, comanda_id):
    """
    Tela principal da comanda: mostra os itens, o total, e os
    formularios para adicionar novos pratos/combos.
    """
    comanda = get_object_or_404(Comanda, pk=comanda_id)

    contexto = {
        'comanda': comanda,
        'itens': comanda.itens.select_related('prato', 'combo'),
        'form_prato': AdicionarPratoForm(),
        'form_combo': AdicionarComboForm(),
    }
    return render(request, 'comandas/comanda_detail.html', contexto)


def adicionar_prato(request, comanda_id):
    comanda = get_object_or_404(Comanda, pk=comanda_id, status='aberta')

    if request.method == 'POST':
        form = AdicionarPratoForm(request.POST)
        if form.is_valid():
            ItemComanda.objects.create(
                comanda=comanda,
                prato=form.cleaned_data['prato'],
                quantidade=form.cleaned_data['quantidade'],
                preco_unitario=form.cleaned_data['prato'].preco,
            )
            messages.success(request, 'Prato adicionado a comanda.')

    return redirect('comandas:detalhe_comanda', comanda_id=comanda.pk)


def adicionar_combo(request, comanda_id):
    comanda = get_object_or_404(Comanda, pk=comanda_id, status='aberta')

    if request.method == 'POST':
        form = AdicionarComboForm(request.POST)
        if form.is_valid():
            ItemComanda.objects.create(
                comanda=comanda,
                combo=form.cleaned_data['combo'],
                quantidade=form.cleaned_data['quantidade'],
                preco_unitario=form.cleaned_data['combo'].preco,
            )
            messages.success(request, 'Combo adicionado a comanda.')

    return redirect('comandas:detalhe_comanda', comanda_id=comanda.pk)


def alterar_quantidade(request, item_id):
    item = get_object_or_404(ItemComanda, pk=item_id, comanda__status='aberta')

    if request.method == 'POST':
        form = AlterarQuantidadeForm(request.POST)
        if form.is_valid():
            item.quantidade = form.cleaned_data['quantidade']
            item.save()
            messages.success(request, 'Quantidade atualizada.')

    return redirect('comandas:detalhe_comanda', comanda_id=item.comanda.pk)


def remover_item(request, item_id):
    item = get_object_or_404(ItemComanda, pk=item_id, comanda__status='aberta')
    comanda_id = item.comanda.pk
    item.delete()
    messages.success(request, 'Item removido da comanda.')
    return redirect('comandas:detalhe_comanda', comanda_id=comanda_id)


def fechar_comanda(request, comanda_id):
    """
    Fecha a conta. So aceitamos POST porque fechar a comanda e uma
    acao que muda o estado do sistema (nao deve acontecer so por
    acessar uma URL via GET, por exemplo, se o usuario atualizar a pagina).
    """
    comanda = get_object_or_404(Comanda, pk=comanda_id, status='aberta')

    if request.method == 'POST':
        comanda.fechar()
        messages.success(request, f'Conta fechada. Total: R$ {comanda.total}')
        return redirect('comandas:detalhe_comanda', comanda_id=comanda.pk)

    return redirect('comandas:detalhe_comanda', comanda_id=comanda.pk)
