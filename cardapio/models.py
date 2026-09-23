from django.db import models


class Prato(models.Model):
    """
    Um item individual do cardapio (ex: 'Feijoada', 'Suco de Laranja').
    """

    # --- Constantes do seu codigo atual (HEAD) ---
    TIPO_ENTRADA = 'entrada'
    TIPO_PRINCIPAL = 'principal'
    TIPO_SOBREMESA = 'sobremesa'
    TIPO_BEBIDA = 'bebida'
    TIPO_ACOMPANHAMENTO = 'acompanhamento'
    TIPO_CHOICES = [
        (TIPO_ENTRADA, 'Entrada'),
        (TIPO_PRINCIPAL, 'Prato Principal'),
        (TIPO_SOBREMESA, 'Sobremesa'),
        (TIPO_BEBIDA, 'Bebida'),
        (TIPO_ACOMPANHAMENTO, 'Acompanhamento'),
    ]

    # --- Constantes exigidas pelo Patch (Feature 1) ---
    CATEGORIA_ENTRADA = 'entrada'
    CATEGORIA_PRATO_PRINCIPAL = 'prato_principal'
    CATEGORIA_SOBREMESA = 'sobremesa'
    CATEGORIA_BEBIDA = 'bebida'
    CATEGORIA_CHOICES = [
        (CATEGORIA_ENTRADA, 'Entrada'),
        (CATEGORIA_PRATO_PRINCIPAL, 'Prato Principal'),
        (CATEGORIA_SOBREMESA, 'Sobremesa'),
        (CATEGORIA_BEBIDA, 'Bebida'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    
    # Campo "categoria" exigido pelo patch 0001
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIA_CHOICES,
        default=CATEGORIA_PRATO_PRINCIPAL,
    )
    
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    
    # Campo "tipo" preservado do seu codigo original
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default=TIPO_PRINCIPAL)
    
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