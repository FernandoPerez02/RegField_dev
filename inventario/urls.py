from django.urls import path
from . import views
urlpatterns = [
    path('inventario/', views.inventario, name='inventario'),
    
    path('gestion_inventario/', views.gestion_inventario, name='gestion_inventario'),
    
    
    
    path('agregarproducto/', views.agregarinventario, name='agregarproducto'),
    path('obtenerestado/', views.obtenerestado, name='obtenerestado'),
    path('obtenerproducto/', views.obtenerproducto, name='obtenerproducto'),
    path('editpro/<id_producto>', views.editarinventario, name='editarinventario'),
    path('eliminarpro/<id_producto>', views.eliminar, name='eliminarinventario'),
    
    path('stockin/', views.stockinven, name='gestion_stock'),
    path('agregarstock/', views.agregarstock, name='agregarstock'),
    path('editarstock/<id_stockinven>', views.editarstock, name='editarstock'),
    
    path('inventario-filter/', views.inventario_filter, name='inventario_filter'),  
    
]