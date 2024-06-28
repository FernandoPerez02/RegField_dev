from django.shortcuts import render
from new_user import forms as formuser, views as tenplateuser
# Create your views here.
def hola(request):
    pass

class seleccionarModelo():
    def datesuario(request):
        'usuario' in request.path
        modeloForm = formuser.NewuserForm    
        template = tenplateuser.usuario
        return modeloForm, template
    
    def prueba(request):
        yie = 'hola'
        return yie

def addRegistro(request):
    accesdate = seleccionarModelo()
    modeloForm, template = accesdate.datesuario(request)
    
    tenplateform = template
    
    
    if request.method == 'POST':
        formulario = modeloForm(request.POST)
        formulario.is_valid()
        formulario ['mensaje'] = 'Registro exitoso'
        datos = formulario
        print (datos)
        
    return render(request, formulario)
        
        