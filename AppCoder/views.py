from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def inicio(request):

    return render(request,"AppCoder/inicio.html")

def catalogo(request):

   return render(request,"AppCoder/catalogo.html")

def vendedores(request):

    return render(request,"AppCoder/vendedores.html")
    #al seleccionar el vendedor te va a abrir la pagina catalogo con el filtro del vendedor, si se puede

def mi_usuario(request,name):

    return render(request,"AppCoder/mi_usuario.html")
    #la pagina del usuario, donde pueda acceder a sus compras y a sus caracteristicas de usuario



