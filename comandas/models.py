from django.db import models
from restaurante.models import Mesa
from cardapio.models import Prato, Combo


class Comanda(models.Model):
    """
    Representa a 'conta' aberta em uma mesa. Uma comanda comeca
    aberta, recebe itens, e no final e fechada (fechamento da conta).
    """

    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('fechada', 'Fechada'),
    ]

    mesa = models.ForeignKey(
        Mesa,
        on_delete=models.PROTECT,   # nao deixa apagar uma mesa que tem comanda vinculada
        related_name='comandas'
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aberta')
    aberta_em = models.DateTimeField(auto_now_add=True)  # preenchido automaticamente na criacao
    fechada_em = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Comanda #{self.pk} - {self.mesa} ({self.status})'

    @property
    def total(self):
        """
        Soma o subtotal de todos os itens da comanda.
        """
        return sum((item.subtotal for item in self.itens.all()), 0)

    def fechar(self):
        """
        Fecha a comanda: muda o status e registra o horario de fechamento.
        """
        from django.utils import timezone
        self.status = 'fechada'
        self.fechada_em = timezone.now()
        self.save()


class ItemComanda(models.Model):
    """
    Cada linha da comanda: um prato OU um combo, com quantidade.
    """
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE, related_name='itens')
    prato = models.ForeignKey(Prato, on_delete=models.PROTECT, null=True, blank=True)
    combo = models.ForeignKey(Combo, on_delete=models.PROTECT, null=True, blank=True)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self, *args, **kwargs):
        # Pega o preco do prato ou combo relacionado na hora de salvar.
        if not self.preco_unitario:
            self.preco_unitario = self.prato.preco if self.prato else self.combo.preco
        super().save(*args, **kwargs)

    @property
    def subtotal(self):
        return self.preco_unitario * self.quantidade

    @property
    def nome_item(self):
        return self.prato.nome if self.prato else self.combo.nome

    def __str__(self):
        return f'{self.quantidade}x {self.nome_item}'
