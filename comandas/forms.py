from django import forms
from cardapio.models import Prato, Combo


class AdicionarPratoForm(forms.Form):
    """
    Form simples (nao e ModelForm) porque queremos limitar as opcoes
    de prato apenas aos disponiveis, e nao precisamos salvar direto -
    a logica de criar o ItemComanda fica na view.
    """
    prato = forms.ModelChoiceField(queryset=Prato.objects.filter(disponivel=True))
    quantidade = forms.IntegerField(min_value=1, initial=1)


class AdicionarComboForm(forms.Form):
    combo = forms.ModelChoiceField(queryset=Combo.objects.filter(disponivel=True))
    quantidade = forms.IntegerField(min_value=1, initial=1)


class AlterarQuantidadeForm(forms.Form):
    quantidade = forms.IntegerField(min_value=1)
