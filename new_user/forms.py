from django import forms
from . import models

class NewuserForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ['rol', 'usuario', 'correo', 'contrasena']