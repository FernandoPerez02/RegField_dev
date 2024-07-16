from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .forms import Empleadoform
from gestion import models

# Create your views here.


def editarempleado(request, id_empleado):
    regedit = get_object_or_404(models.Empleado, id_empleado=id_empleado)
    
    data = {
        'form': Empleadoform(instance=regedit)
    }
    
    if request.method == 'POST':
        formulario = Empleadoform(request.POST, instance=regedit)    
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Edicion Exitosa'
            
        else:
            data['mensaje'] = 'Edicion fallida'
    
    listar_empleado = models.Empleado.objects.all()
    
    return render(request, 'editarempleado.html', {'data': data, 'listar_empleado': listar_empleado})


def obtenerestado(request):
    estado = models.Estado.objects.all().values('id_estado', 'estado')
    return JsonResponse(list(estado), safe=False)

def empleado(request):
    listar_empleado = models.Empleado.objects.all()
    return render(request, 'empleado.html', {'listar_empleado':listar_empleado})


def agregaregistroemple(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        documento = request.POST['documento']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        fecha = request.POST['fecha']
        id_estado = request.POST['id_estado']

        
        estado = models.Estado.objects.get(id_estado=id_estado)

        form_data = {
            'nombre': nombre,
            'apellido': apellido,
            'documento': documento,
            'telefono': telefono,
            'correo': correo,
            'fecha': fecha,
            'id_estado': estado  
        }

        form = Empleadoform(form_data)
        if form.is_valid():
            form.save()
            return redirect('empleado')  

  
    return redirect('empleado')
    
def eliminar(request, id_empleado):
    registro = get_object_or_404(models.Empleado, id_empleado=id_empleado)
    registro.delete()
    return redirect('empleado')

