from django.urls import path
from . import views as v

urlpatterns = [
    path('usuarios/', v.usuarios, name='usuarios'),
    path('editarusuarios/<id_usuario>', v.editarusuarios, name='editarusuarios'),
    path('eliminarusuarios/<id_usuario>', v.eliminar, name='eliminarusuarios'),
]
