from django.urls import path
from . import views 

urlpatterns = [
    path('agregaregistroemple/', views.agregaregistroemple, name='agregaregistroemple'),
    path('obtenerestado/', views.obtenerestado, name='obtenerestado'),
    path('empleados/', views.empleados, name='empleados'),
    path('editaremple/<id_empleado>', views.editaremple, name='editaremple'),
    path('eliminaremple/<id_empleado>', views.eliminar, name='eliminaremple'),
]
