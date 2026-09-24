"""
URLs principais do projeto. Aqui nao colocamos a logica das paginas,
apenas "encaminhamos" cada prefixo de URL para o urls.py do app correto,
usando include(). Isso mantem cada app responsavel pelas suas proprias rotas.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='cardapio/pratos/'), name='home'),
    path('cardapio/', include('cardapio.urls')),
    path('restaurante/', include('restaurante.urls')),
    path('comandas/', include('comandas.urls')),
]
