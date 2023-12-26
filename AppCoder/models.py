from django.db import models

# Create your models here.
class vendedor(models.Model):
    nombre=models.CharField(max_length=99)
    cuit=models.CharField(max_length=20)
    email=models.EmailField()
    insumos=models.CharField(max_length=20)

class insumo(models.Model):
    nombre=models.CharField(max_length=99)
    tipo=models.CharField(max_length=20)
    unidad=models.CharField(max_length=20)
    precio_unidad=models.IntegerField()
    stock=models.IntegerField()

class usuario(models.Model):
    usuario=models.CharField(max_length=99)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    compras=models.CharField(max_length=20)