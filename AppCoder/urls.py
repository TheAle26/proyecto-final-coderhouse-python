from django.urls import path
from AppCoder import views

urlpatterns=[
    path('inicio',views.inicio),
    path('catalogo',views.catalogo),
    path('vendedores',views.vendedores),
    path('mi_usuario',views.mi_usuario),

]