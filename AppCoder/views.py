from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Restaurantes


def resto(request):
    rest1=Restaurantes(nombre="La Modelo",camada=4.5)
    rest1.save()
    return HttpResponse(f"Se ha creado el restaurante {rest1.nombre}")
# Create your views here.
