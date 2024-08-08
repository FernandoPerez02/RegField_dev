from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from gestion import forms, models
from django.http import HttpResponse

# Create your views here.
def config(request):
    datosFinca = models.DatosFinca.objects.all()
    return render(request, 'configuraciones.html', {'datosFinca':datosFinca})

def agregarconfi(request):
    if request.method == 'POST':
        nit_finca = request.POST.get('nit_finca')
        nombre_finca = request.POST.get('nombre_finca')
        nombre_responsable = request.POST.get('nombre_responsable')
        telefono_responsable = request.POST.get('telefono_responsable')
        direccion = request.POST.get('direccion')
                 
        form_data = {
            'nit_finca': nit_finca,
            'nombre_finca': nombre_finca,
            'nombre_responsable': nombre_responsable,
            'telefono_responsable': telefono_responsable,
            'direccion': direccion              
        }
     
        form = forms.confiForm(form_data)
        if form.is_valid():
            form.save()
    return redirect('config')

def editarfinca(request, id_configuracion):
    datosFinca = models.DatosFinca.objects.all()
    regedit = get_object_or_404(models.DatosFinca, id_configuracion=id_configuracion)
    
    data = {
        'form': forms.FincaForm(instance=regedit)
    }
    
    if request.method == 'POST':
        formulario = forms.FincaForm(request.POST, instance=regedit)    
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Edicion Exitosa'
            
        else:
            data['mensaje'] = 'Edicion fallida'
    return render(request, 'configuraciones.html', {'datosFinca': datosFinca, 'data': data})

def eliminarfinca(request,id_configuracion):
    regeditfinca = get_object_or_404(models.DatosFinca, id_configuracion=id_configuracion)
    regeditfinca.delete()
    return redirect('registrarfinca')