from django.db import models

# Create your models here.
class vendedor(models.Model):
    nombre=models.CharField(max_length=99)
    cuit=models.CharField()
    email=models.EmailField()
    insumos=models.CharField()

class insumo(models.Model):
    nombre=models.CharField(max_length=99)
    unidad=models.CharField()
    precio_unidad=models.IntegerField()
    stock=models.CharField()
    
class usuario(models.Model):
    usuario=models.CharField(max_length=99)
    password=models.CharField()
    email=models.EmailField()
    compras=models.CharField()