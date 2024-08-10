from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from .forms import Laborform
from gestion import models
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

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
    
    return render(request, 'editarlabor.html', {'data': data, 'listar_labor': listar_labor})

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
    registros = models.Labor.objects.all()  # Obtiene todos los registros del modelo. Ajusta según tu consulta.
    context = {'data': registros}  # Crea un contexto con los datos obtenidos.
    pdf = render_to_pdf('labor_pdf.html', context)  # Llama a render_to_pdf para generar el PDF.
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="inventario.pdf"' 
        return response
    return HttpResponse("Error al generar el PDF", status=500)