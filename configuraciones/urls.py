from django.urls import path
from . import views

urlpatterns = [
    path('confi/', views.config, name='confi'),
    path('agregarfinca/', views.agregarconfi, name='agregarfinca'),
    path('editarfinca/<id_configuracion>', views.editarfinca, name='editarfinca'),
    path('eliminarfinca/<id_configuracion>', views.eliminarfinca, name='eliminarfinca'),
]