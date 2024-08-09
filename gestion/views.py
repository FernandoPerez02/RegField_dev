from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .forms import Manejocafeform
from . import models
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO


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
    
    return render(request, 'editar_cafe.html', {'data': data, 'listarecoleccion': listar_recoleccion})


def obtener_empleados(request):
    empleados = models.Empleado.objects.all().values('id_empleado', 'nombre')
    return JsonResponse(list(empleados), safe=False)

def obtener_tiporegistro(request):
    tipo = models.TipoRegistro.objects.all().values('id_tipo_registro', 'tipo_registro')
    return JsonResponse(list(tipo), safe=False)

def agregaregistrocafe(request):
    if request.method == 'POST':
        id_empleado = request.POST['id_empleado']
        peso = request.POST['peso']
        id_tipo_registro = request.POST['id_tipo_registro']
        fecha = request.POST['fecha']
        
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
    return render(request, 'Manejo_cafe.html', {'listarecoleccion':listar_recoleccion})
   
def eliminar(request, id_cafe):
    registro = get_object_or_404(models.ManejoCafe, id_cafe=id_cafe)
    registro.delete()
    return redirect('gestioncafe')

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
    registros = models.ManejoCafe.objects.all()  # Obtiene todos los registros del modelo. Ajusta según tu consulta.
    context = {'data': registros}  # Crea un contexto con los datos obtenidos.
    pdf = render_to_pdf('cafe_pdf.html', context)  # Llama a render_to_pdf para generar el PDF.
    return pdf  # Devuelve el PDF generado como respuesta.
