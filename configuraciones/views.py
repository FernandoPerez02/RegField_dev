from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from gestion import forms
from django.http import HttpResponse

# Create your views here.
def config(request):
    return render(request, 'configuraciones.html')

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
            return HttpResponse('Fallo')
        else:
            return HttpResponse('fallo')
            print(form.errors)  # Paso para depuración
    return redirect('config')
