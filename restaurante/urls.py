from django.urls import path
from . import views

app_name = 'restaurante'

urlpatterns = [
    path('mesas/', views.lista_mesas, name='lista_mesas'),
]
