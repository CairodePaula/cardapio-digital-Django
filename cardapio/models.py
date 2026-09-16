from django.db import models


class Prato(models.Model):
    """
    Um item individual do cardapio (ex: 'Feijoada', 'Suco de Laranja').
    """

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

    CATEGORIA_BRASILEIRA = 'brasileira'
    CATEGORIA_ITALIANA = 'italiana'
    CATEGORIA_JAPONESA = 'japonesa'
    CATEGORIA_VEGETARIANA = 'vegetariana'
    CATEGORIA_VEGANA = 'vegana'
    CATEGORIA_OUTRA = 'outra'
    CATEGORIA_CHOICES = [
        (CATEGORIA_BRASILEIRA, 'Brasileira'),
        (CATEGORIA_ITALIANA, 'Italiana'),
        (CATEGORIA_JAPONESA, 'Japonesa'),
        (CATEGORIA_VEGETARIANA, 'Vegetariana'),
        (CATEGORIA_VEGANA, 'Vegana'),
        (CATEGORIA_OUTRA, 'Outra'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default=TIPO_PRINCIPAL)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default=CATEGORIA_OUTRA)
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
