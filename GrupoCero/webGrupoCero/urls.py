from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[

    path('', index, name='IND'),
    path('galeria/', galeria, name='GALE'),
    path('artistas/', artistas, name='ART'),
    path('perfil/', perfil, name='PERF'),
    path('ingreso/', ingreso, name= 'ING'),
    path('descripcion/<id>',descripcion,name='DES'),
    path('contacto/', contacto , name = 'CONT'),
    path('mensaje/', mensaje , name= 'MENS'),
    path('olvide/', recuperacion , name='OLV'),
    path('logout/',cerrar_sesion, name='LOGOUT'),
    path('registro/', registro, name='REG'),
    path('filtro_cate/',filtro_cate,name='FILTRO_CATE'),
    path('filtro_categoria/<id>/',filtro_categoria,name='FILTRO_CATEGORIA'),
    path('buscar/', busca, name='BUSC'),
    path('verificar-usuario/', verificar_usuario, name='verificar_usuario'),
    path('carrito/', carrito, name='CAR')

]