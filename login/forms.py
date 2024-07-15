from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=15, required=True)
    contrasena = forms.CharField(widget=forms.PasswordInput, required=True)
