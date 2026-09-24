from django import forms
from .models import Prato


class PratoForm(forms.ModelForm):
    """
    Formulario de cadastro/edicao de Prato.

    Feature 2 (validacao customizada): o preco do prato precisa ser
    maior que zero. O Django ja garante que o campo 'preco' seja
    preenchido e seja um numero valido (obrigatorio + tipo, de graca),
    mas nao impede um valor zero ou negativo - isso e regra de negocio
    do cardapio, entao validamos aqui.
    """

    class Meta:
        model = Prato
        fields = ['nome', 'descricao', 'categoria', 'preco', 'disponivel']

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco is not None and preco <= 0:
            raise forms.ValidationError('O preço do prato deve ser maior que zero.')
        return preco
