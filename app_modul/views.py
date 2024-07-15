from django.shortcuts import render, redirect, get_object_or_404
from regfield.decoractors import login_required
from gestion.models import ManejoCafe, DatosFinca
import json
from django.db.models import Sum
from gestion.forms import FincaForm
from django.http import HttpResponse

# Create your views here.
def base(request):
    nameFinca = DatosFinca.objects.all().values('nombre_finca')
    return render(request, 'base.html', {'nameFinca':nameFinca})

@login_required
def inicio(request):
    kilos = ManejoCafe.objects.all().values('fecha').annotate(total_peso=Sum('peso'))
    
    for item in kilos:
        item['fecha'] = item['fecha'].isoformat()
    kilos_json = json.dumps(list(kilos))  # Serializa el queryset a JSON
    context = {
        'kilos': kilos_json
    }
    return render(request, 'inicio.html', context)

def finca(request):
    datosFinca = DatosFinca.objects.all()
    return render(request, 'datos_finca.html', {'datosFinca': datosFinca})

def reguistrarfinca(request):
    if request.method == 'POST':
        nit_finca = request.POST['nit_finca']
        nombre_finca = request.POST['nombre_finca']
        nombre_responsable = request.POST['nombre_responsable']
        telefono_responsable = request.POST['telefono_responsable']
        direccion = request.POST['direccion']
        
        form_data = {
            'nit_finca': nit_finca,
            'nombre_finca': nombre_finca,
            'nombre_responsable': nombre_responsable,
            'telefono_responsable': telefono_responsable,
            'direccion': direccion
            }
        
        form = FincaForm(form_data)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse('registro fallido')
        
        return redirect('gestionfinca')

def editarfinca(request, id_configuracion):
    datosFinca = DatosFinca.objects.all()
    regedit = get_object_or_404(DatosFinca, id_configuracion=id_configuracion)
    
    data = {
        'form': FincaForm(instance=regedit)
    }
    
    if request.method == 'POST':
        formulario = FincaForm(request.POST, instance=regedit)    
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Edicion Exitosa'
            
        else:
            data['mensaje'] = 'Edicion fallida'
    return render(request, 'editarfinca.html', {'datosFinca': datosFinca, 'data': data})

def eliminarfinca(request,id_configuracion):
    regeditfinca = get_object_or_404(DatosFinca, id_configuracion=id_configuracion)
    regeditfinca.delete()
    return redirect('registrarfinca')
