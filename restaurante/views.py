from django.shortcuts import render
from .models import Mesa


def lista_mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'restaurante/mesas_list.html', {'mesas': mesas})
