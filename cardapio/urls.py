from django.urls import path
from . import views

app_name = 'cardapio'

urlpatterns = [
    path('pratos/', views.lista_pratos, name='lista_pratos'),
    path('combos/', views.lista_combos, name='lista_combos'),
]
