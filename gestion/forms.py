from django import forms
from .models import ManejoCafe, DatosFinca, Inventario, StockInventario

class Manejocafeform(forms.ModelForm):
    class Meta:
        model = ManejoCafe
        fields = ['peso', 'fecha', 'id_tipo_registro', 'id_empleado']
        
class FincaForm(forms.ModelForm):
    class Meta:
        model = DatosFinca
        fields = ['nit_finca', 'nombre_finca', 'nombre_responsable', 'telefono_responsable', 'direccion']

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['producto', 'descripcion', 'categoria', 'fecha', 'id_tipo_registro', 'id_estado']
        
class StockinvenForm(forms.ModelForm):
    class Meta:
        model = StockInventario
        fields = ['cantidad', 'unidad_medida', 'id_producto', 'id_tipo_registro']
        
class confiForm(forms.ModelForm):
    class Meta:
        model = DatosFinca
        fields = ['nit_finca', 'nombre_finca', 'nombre_responsable', 'telefono_responsable', 'direccion']