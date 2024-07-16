from django import forms
from gestion.models import Empleado

class Empleadoform(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['id_empleado', 'nombre', 'apellido', 'documento', 'telefono', 'correo', 'fecha',  'id_estado']