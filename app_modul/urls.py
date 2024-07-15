from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('finca/', views.finca, name='finca'),
    path('base/', views.base, name='base'),
    path('registrarfinca/', views.reguistrarfinca, name='registrarFinca'),
    path('editarfinca/<id_configuracion>', views.editarfinca, name='editarfinca'),
    path('eliminarfinca/<id_configuracion>', views.eliminarfinca, name='eliminarfinca'),
]