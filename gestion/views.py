from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .froms import Manejocafeform
from . import models


# Create your views here.

""" Manejo de cafe """
def editar(request, id_cafe):
    regedit = get_object_or_404(models.ManejoCafe, id_cafe=id_cafe)
    
    data = {
        'form': Manejocafeform(instance=regedit)
    }
    
    if request.method == 'POST':
        formulario = Manejocafeform(request.POST, instance=regedit)    
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Edicion Exitosa'
            
        else:
            data['mensaje'] = 'Edicion fallida'
    
    listar_recoleccion = models.ManejoCafe.objects.all()
    
    return render(request, 'editar.html', {'data': data, 'listarecoleccion': listar_recoleccion})


def obtener_empleados(request):
    empleados = models.Empleado.objects.all().values('id_empleado', 'nombre')
    return JsonResponse(list(empleados), safe=False)

def obtener_tiporegistro(request):
    tipo = models.TipoRegistro.objects.all().values('id_tipo_registro', 'tipo_registro')
    return JsonResponse(list(tipo), safe=False)

def cafe(request):
    listar_recoleccion = models.ManejoCafe.objects.all()
    return render(request, 'manejo_cafe.html', {'listarecoleccion':listar_recoleccion})


def agregaregistrocafe(request):
    if request.method == 'POST':
        id_empleado = request.POST['id_empleado']
        peso = request.POST['peso']
        id_tipo_registro = request.POST['id_tipo_registro']
        fecha = fecha = request.POST['fecha']
        
        form_data = {
            'id_empleado': id_empleado,
            'peso': peso,
            'id_tipo_registro': id_tipo_registro, 
            'fecha': fecha
            }
        
        form = Manejocafeform(form_data)
        if form.is_valid():
            form.save()
        
        return redirect('gestioncafe')
        
    
def gestioncafe(request):
    listar_recoleccion = models.ManejoCafe.objects.all()
    return render(request, 'Editarcafe.html', {'listarecoleccion':listar_recoleccion})
    
def eliminar(request, id_cafe):
    registro = get_object_or_404(models.ManejoCafe, id_cafe=id_cafe)
    registro.delete()
    return redirect('gestioncafe')
            



        
    