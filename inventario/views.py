from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from gestion import forms, models
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO


# Create your views here.
def obtenerestado(request):
    listestado = models.Estado.objects.all().values('id_estado', 'estado')
    return JsonResponse(list(listestado), safe=False)

def obtenerproducto(request):
    listproducto = models.Inventario.objects.all().values('id_producto', 'producto')
    return JsonResponse(list(listproducto), safe=False)

def inventario(request):
    context = inventario_filter()
    return render (request, 'inventario.html',{'context':context})

def gestion_inventario(request):
    listinven = models.Inventario.objects.all()
    return render(request, 'gestion_inventario.html', {'listinven': listinven})

def agregarinventario(request):
    if request.method == 'POST':
            producto = request.POST['producto']
            descripcion = request.POST['descripcion']
            categoria = request.POST['categoria']
            fecha = request.POST['fecha']
            id_estado = request.POST['id_estado']
            
            data_inve = {
                'producto': producto,
                'descripcion': descripcion,
                'categoria': categoria,
                'fecha': fecha,
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
    stocklist = models.StockInventario.objects.all()
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
              
    return render(request, 'editarstock.html', {'data': data, 'stocklist':stocklist }) 

""" Pruebas  """
def inventario_list(request):
    inventarios = models.Inventario.objects.all()
    return render(request, 'inventario_list.html', {'inventarios': inventarios})

def inventario_create(request):
    if request.method == 'POST':
        form = forms.InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = forms.InventarioForm()
    return render(request, 'inventario_form.html', {'form': form})

def inventario_filter():
    inventarios = models.Inventario.objects.all()
    producto_data = []

    for inventario in inventarios:
        # Obtener registros de entrada y salida
        input_records = models.StockInventario.objects.filter(id_producto=inventario, id_tipo_registro__tipo_registro='Ingreso')
        output_records = models.StockInventario.objects.filter(id_producto=inventario, id_tipo_registro__tipo_registro='Salida')

        # Calcular las cantidades de entrada y salida
        input_quantity = sum(record.cantidad for record in input_records)
        output_quantity = sum(record.cantidad for record in output_records)

        # Calcular la cantidad actual
        current_quantity = input_quantity - output_quantity

        producto_data.append({
            'producto': inventario.producto,
            'descripcion': inventario.descripcion,
            'categoria': inventario.categoria,
            'estado': inventario.id_estado,
            'cantidad_actual': current_quantity,
        })

    context = {
        'producto_data': producto_data,
    }

    return context

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)  # Carga la plantilla HTML.
    html = template.render(context_dict)  # Renderiza la plantilla con el contexto proporcionado.
    result = BytesIO()  # Crea un objeto BytesIO para manejar los datos del PDF en memoria.
    pdf = pisa.CreatePDF(BytesIO(html.encode('utf-8')), dest=result)  # Convierte el HTML a PDF.
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')  # Devuelve el PDF como respuesta HTTP.
    return None  # Si ocurre un error en la conversión, devuelve None.


def download_pdf(request):
    # Obtén los datos de la base de datos
    registros = models.Inventario.objects.all()  # Obtiene todos los registros del modelo. Ajusta según tu consulta.
    context = {'data': registros}  # Crea un contexto con los datos obtenidos.
    pdf = render_to_pdf('inventario_pdf.html', context)  # Llama a render_to_pdf para generar el PDF.
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="inventario.pdf"' 
        return response
    return HttpResponse("Error al generar el PDF", status=500)
