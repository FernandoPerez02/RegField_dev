from django.urls import path
from . import views 

urlpatterns = [
    path('agregaregistroemple/', views.agregaregistroemple, name='agregaregistroemple'),
    path('obtenerestado/', views.obtenerestado, name='obtenerestado'),
    path('empleado/', views.empleado, name='empleado'),
    path('editarempleado/<id_empleado>', views.editarempleado, name='editarempleado'),
    path('eliminaremple/<id_empleado>', views.eliminar, name='eliminaremple'),
]