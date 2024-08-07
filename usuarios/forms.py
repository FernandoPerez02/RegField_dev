from django import forms
from gestion import models

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ['rol', 'usuario', 'gmail', 'contrasena']