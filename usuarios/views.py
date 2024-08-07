from django.shortcuts import render, get_object_or_404, redirect
from .forms import UsuariosForm
from gestion import models
# Create your views here.

def editarusuarios(request, id_usuario):
    regedit = get_object_or_404(models.Usuario, id_usuario=id_usuario)
    
    data = {
        'form': UsuariosForm(instance=regedit)
    }
    
    if request.method == 'POST':
        formulario = UsuariosForm(request.POST, instance=regedit)    
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Edicion Exitosa'
            
        else:
            data['mensaje'] = 'Edicion fallida'
    
    listar_usuarios = models.Usuario.objects.all()
    
    return render(request, 'editarusuarios.html', {'data': data, 'listar_usuarios': listar_usuarios})


def usuarios(request):
    listar_usuarios = models.Usuario.objects.all()
    return render(request, 'usuarios.html', {'listar_usuarios':listar_usuarios})

def eliminar(request, id_usuario):
    registro = get_object_or_404(models.Usuario, id_usuario=id_usuario)
    registro.delete()
    return redirect('usuarios')



