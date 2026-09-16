from django.urls import path
from . import views

app_name = 'comandas'

urlpatterns = [
    path('abrir/<int:mesa_id>/', views.abrir_comanda, name='abrir_comanda'),
    path('<int:comanda_id>/', views.detalhe_comanda, name='detalhe_comanda'),
    path('<int:comanda_id>/adicionar-prato/', views.adicionar_prato, name='adicionar_prato'),
    path('<int:comanda_id>/adicionar-combo/', views.adicionar_combo, name='adicionar_combo'),
    path('<int:comanda_id>/fechar/', views.fechar_comanda, name='fechar_comanda'),
    path('item/<int:item_id>/alterar-quantidade/', views.alterar_quantidade, name='alterar_quantidade'),
    path('item/<int:item_id>/remover/', views.remover_item, name='remover_item'),
]
