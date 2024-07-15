from django.urls import path
from . import views 

urlpatterns = [
    path('agregaregistrolabor/', views.agregaregistrolabor, name='agregaregistrolabor'),
    path('obtenerempleado/', views.obtenerempleado, name='obtenerempleado'),
    path('obtenerestado/', views.obtenerestado, name='obtenerestado'),
    path('labor/', views.labor, name='labor'),
    path('editarlabor/<id_labor>', views.editarlabor, name='editarlabor'),
    path('eliminarlabor/<id_labor>', views.eliminar, name='eliminarlabor')
]