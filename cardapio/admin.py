from django.contrib import admin
from .models import Prato, Combo


@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'categoria', 'preco', 'disponivel')
    list_filter = ('tipo', 'categoria', 'disponivel')
    search_fields = ('nome',)


admin.site.register(Combo)
