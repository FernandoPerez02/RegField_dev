from django.urls import path
from . import views 

urlpatterns = [
    path('agregaregistrocafe/', views.agregaregistrocafe, name='agregaregistrocafe'),
    path('obtener_empleados/', views.obtener_empleados, name='obtenerempleado'),
    path('obtener_tipo/', views.obtener_tiporegistro, name='obtenertiporegistro'),
    path('gestioncafe/', views.gestioncafe, name='gestioncafe'),
    path('editarcafe/<id_cafe>', views.editar, name='editarcafe'),
    path('eliminar/<id_cafe>', views.eliminar, name='delete')
]