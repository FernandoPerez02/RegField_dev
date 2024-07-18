from django import forms
from gestion.models import Labor

class Laborform(forms.ModelForm):
    class Meta:
        model = Labor
        fields = ['id_labor', 'descripcion', 'lote', 'fecha_labor', 'id_empleado']