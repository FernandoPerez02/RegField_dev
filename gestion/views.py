from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .forms import Manejocafeform
from . import models
from django.db.models import Sum


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


from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date
from django.db.models import Sum
from xhtml2pdf import pisa
import io
from . import models

def validar_fecha(fecha_str):
    """Valida que la fecha esté en formato YYYY-MM-DD y devuelve la fecha en formato datetime.date."""
    try:
        fecha = parse_date(fecha_str)
        if fecha is None:
            raise ValidationError('La fecha debe estar en formato YYYY-MM-DD.')
        return fecha
    except ValueError:
        raise ValidationError('La fecha debe estar en formato YYYY-MM-DD.')

def render_to_pdf(template_src, context_dict):
    """Convierte una plantilla HTML a un archivo PDF."""
    template = render_to_string(template_src, context_dict)
    result = io.BytesIO()
    pdf = pisa.CreatePDF(io.BytesIO(template.encode("UTF-8")), dest=result)
    if not pdf.err:
        return result.getvalue()
    return None

def descargar_pdf(request):
    fecha_inicio_str = request.GET.get('fecha_inicio')
    fecha_fin_str = request.GET.get('fecha_fin')
    agrupacion = request.GET.get('agrupacion')
    tipo_registro = request.GET.get('tipo_registro')
    
    try:
        fecha_inicio = validar_fecha(fecha_inicio_str)
        fecha_fin = validar_fecha(fecha_fin_str)
    except ValidationError as e:
        return HttpResponse(f"Error: {e}", status=400)

    # Filtrar registros por el rango de fechas
    registros = models.ManejoCafe.objects.filter(
        fecha__range=[fecha_inicio, fecha_fin],
        tipo_registro=tipo_registro
    )

    # Agrupación de datos
    if agrupacion == 'empleado':
        registros = registros.values('empleado').annotate(total_kilos=Sum('kilos'))
    else:
        registros = registros

    # Convertir fechas a formato YYYY-MM-DD
    registros_formateados = []
    for registro in registros:
        fecha_formateada = registro.fecha.strftime('%Y-%m-%d') if hasattr(registro, 'fecha') else None
        registro_dict = {
            **registro,
            'fecha': fecha_formateada,
        }
        registros_formateados.append(registro_dict)
    
    context = {
        'registros': registros_formateados,
    }
    
    pdf = render_to_pdf('reporte_pdf.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        return response
    return HttpResponse("Error generating PDF")



import pandas as pd
from django.http import HttpResponse


def descargar_excel(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    agrupacion = request.GET.get('agrupacion')
    tipo_registro = request.GET.get('tipo_registro')
    
    registros = models.ManejoCafe.objects.filter(
        fecha__range=[fecha_inicio, fecha_fin],
        tipo_registro=tipo_registro
    )

    # Agrupación de datos (ajusta esto según tus necesidades)
    if agrupacion == 'empleado':
        registros = registros.values('empleado').annotate(total_kilos=Sum('kilos'))

    df = pd.DataFrame(list(registros))
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="report.xlsx"'
    df.to_excel(response, index=False)
    return response




            



        
    