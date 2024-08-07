from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .forms import Laborform
from gestion import models

# Editar Labor
def editarlabor(request, id_labor):
    regedit = get_object_or_404(models.Labor, id_labor=id_labor)
    
    data = {
        'form': Laborform(instance=regedit)
    }
    
    if request.method == 'POST':
        formulario = Laborform(request.POST, instance=regedit)    
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Edicion Exitosa'
            
        else:
            data['mensaje'] = 'Edicion fallida'
    
    listar_labor = models.Labor.objects.all()
    
    return render(request, 'editar.html', {'data': data, 'listar_labor': listar_labor})

# Obtener Estados
def obtenerestado(request):
    estado = models.Estado.objects.all().values('id_estado', 'estado')
    return JsonResponse(list(estado), safe=False)

# Obtener Empleados
def obtenerempleado(request):
    empleados = models.Empleado.objects.all().values('id_empleado', 'nombre')
    return JsonResponse(list(empleados), safe=False)

# Listar Labores
def labor(request):
    listar_labor = models.Labor.objects.select_related('id_empleado').all()
    return render(request, 'labor.html', {'listar_labor': listar_labor})

# Agregar Registro de Labor
def agregaregistrolabor(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion', '')
        lote = request.POST.get('lote', '')
        fecha_labor = request.POST.get('fecha_labor', '')
        id_empleado = request.POST.get('id_empleado', '')
        empleado = models.Empleado.objects.get(id_empleado=id_empleado)

        form_data = {
            'descripcion': descripcion,
            'lote': lote,
            'fecha_labor': fecha_labor,
            'id_empleado': empleado,
        }

        form = Laborform(form_data)
        if form.is_valid():
            form.save()
            return redirect('labor')

    return redirect('labor')

# Eliminar Labor
def eliminar(request, id_labor):
    registro = get_object_or_404(models.Labor, id_labor=id_labor)
    registro.delete()
    return redirect('labor')