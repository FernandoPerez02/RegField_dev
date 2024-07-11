from django import forms
from .models import ManejoCafe

class Manejocafeform(forms.ModelForm):
    class Meta:
        model = ManejoCafe
        fields = ['peso', 'fecha', 'id_tipo_registro', 'id_empleado']