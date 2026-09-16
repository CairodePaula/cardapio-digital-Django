from django.db import models


class Prato(models.Model):
    """
    Um item individual do cardapio (ex: 'Feijoada', 'Suco de Laranja').
    """
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Combo(models.Model):
    """
    Um combo agrupa varios pratos por um preco fechado
    (ex: 'Combo Executivo' = prato principal + bebida + sobremesa).
    """
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    pratos = models.ManyToManyField(Prato, related_name='combos', blank=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
