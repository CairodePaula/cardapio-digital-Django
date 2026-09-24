from django.db import models


class Mesa(models.Model):
    """
    Mesa do restaurante. Cada mesa recebe uma comanda quando ocupada.
    """
    numero = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = ['numero']

    def __str__(self):
        return f'Mesa {self.numero}'
