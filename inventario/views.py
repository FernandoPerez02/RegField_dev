from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from gestion import forms, models
from django.http import JsonResponse, HttpResponse


# Create your views here.
def obtenerestado(request):
    listestado = models.Estado.objects.all().values('id_estado', 'estado')
    return JsonResponse(list(listestado), safe=False)

def obtenerproducto(request):
    listproducto = models.Inventario.objects.all().values('id_producto', 'producto')
    return JsonResponse(list(listproducto), safe=False)

def inventario(request):
    listinven = models.Inventario.objects.all()
    return render (request, 'inventario.html',{'listinven': listinven})

def agregarinventario(request):
    if request.method == 'POST':
            producto = request.POST['producto']
            descripcion = request.POST['descripcion']
            categoria = request.POST['categoria']
            fecha = request.POST['fecha']
            id_tipo_registro = request.POST['id_tipo_registro']
            id_estado = request.POST['id_estado']
            
            data_inve = {
                'producto': producto,
                'descripcion': descripcion,
                'categoria': categoria,
                'fecha': fecha,
                'id_tipo_registro':id_tipo_registro,
                'id_estado':id_estado
            }
            
            form = forms.InventarioForm(data_inve)
            if form.is_valid():
                form.save()    
 
    return redirect('inventario')

def editarinventario(request, id_producto):
    listinven = models.Inventario.objects.all()
    proedit = get_object_or_404(models.Inventario, id_producto=id_producto)
    
    data = {
        'form': forms.InventarioForm(instance=proedit)
    }
    
    if request.method == 'POST':
        formulario = forms.InventarioForm(request.POST, instance=proedit)    
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Edición Exitosa'
        else:
            data['mensaje'] = 'Edición Fallida'
    
    return render(request, 'editarpro.html', {'data': data, 'listinven': listinven })

def eliminar(request, id_producto):
    registro = get_object_or_404(models.Inventario, id_producto = id_producto)
    registro.delete()
    return redirect('inventario')


def stockinven(request):
    stocklist = models.StockInventario.objects.all()
    return render(request, 'stockinventario.html', {'stocklist':stocklist})


def agregarstock(request):
    if request.method == 'POST':
        cantidad = request.POST['cantidad']
        unidad_medida = request.POST['unidad_medida']
        id_producto = request.POST['id_producto']
        id_tipo_registro = request.POST['id_tipo_registro']
        
        data_inve = {
            'unidad_medida': unidad_medida,
            'cantidad': cantidad,
            'id_producto': id_producto,
            'id_tipo_registro': id_tipo_registro,
        }
        
        form = forms.StockinvenForm(data_inve)
        if form.is_valid():
            form.save()
            return HttpResponse('exito')     
        else:
            print(form.errors)  # Imprimir errores del formulario para depuración
            return HttpResponse('formulario no válido')  # Respuesta en caso de que el formulario no sea válido
                
    return redirect('stockin')


def editarstock(request, id_stockinven):
    liststock = models.StockInventario.objects.all()
    stockedit = get_object_or_404(models.StockInventario, id_stockinven=id_stockinven)
    
    data = {
        'form': forms.StockinvenForm(instance=stockedit)
    }
    
    if request.method == 'POST':
        formulario = forms.InventarioForm(request.POST, instance=stockedit)    
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Edición Exitosa'
        else:
            data['mensaje'] = 'Edición Fallida'
    
    return render(request, 'editarstock.html', {'data': data, 'liststock': liststock }) 



