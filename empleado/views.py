from django.shortcuts import render, get_object_or_404, redirect
from django.http import  JsonResponse, HttpResponse
from .forms import Empleadoform
from gestion import models
from django.contrib import messages
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
# Create your views here.


def editarempleado(request, id_empleado):
    regedit = get_object_or_404(models.Empleado, id_empleado=id_empleado)
    
    data = {
        'form': Empleadoform(instance=regedit)
    }
    
    if request.method == 'POST':
        formulario = Empleadoform(request.POST, instance=regedit)    
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Edicion Exitosa'
            
        else:
            data['mensaje'] = 'Edicion fallida'
    
    listar_empleado = models.Empleado.objects.all()
    
    return render(request, 'editarempleado.html', {'data': data, 'listar_empleado': listar_empleado})


def obtenerestado(request):
    estado = models.Estado.objects.all().values('id_estado', 'estado')
    return JsonResponse(list(estado), safe=False)

def empleado(request):
    listar_empleado = models.Empleado.objects.all()
    return render(request, 'empleados.html', {'listar_empleado':listar_empleado})


def agregaregistroemple(request):
    if request.method == 'POST':
        # Procesar el formulario
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        documento = request.POST['documento']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        fecha = request.POST['fecha']
        id_estado = request.POST['id_estado']

        estado = models.Estado.objects.get(id_estado=id_estado)

        form_data = {
            'nombre': nombre,
            'apellido': apellido,
            'documento': documento,
            'telefono': telefono,
            'correo': correo,
            'fecha': fecha,
            'id_estado': estado  
        }

        form = Empleadoform(form_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro agregado con éxito')
        else:
            messages.error(request, 'Error al agregar registro')

    return redirect('empleado')
    
def eliminar(request, id_empleado):
    registro = get_object_or_404(models.Empleado, id_empleado=id_empleado)
    registro.delete()
    return redirect('empleado')


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
    registros = models.Empleado.objects.all()  # Obtiene todos los registros del modelo. Ajusta según tu consulta.
    context = {'data': registros}  # Crea un contexto con los datos obtenidos.
    pdf = render_to_pdf('informe_empleado.html', context)  # Llama a render_to_pdf para generar el PDF.
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Empleados.pdf"'
        return response
    return HttpResponse("Error al generar el PDF", status=500)
