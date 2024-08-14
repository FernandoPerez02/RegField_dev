from django.shortcuts import render
from regfield.decoractors import login_required
from gestion.models import ManejoCafe, DatosFinca
import json
from django.http import JsonResponse
from django.db.models import Sum
from . import forms
from django.db.models.functions import TruncDay, TruncMonth, TruncYear
from datetime import datetime


# Create your views here.
def base(request):
    nameFinca = DatosFinca.objects.all().values('nombre_finca')
    return render(request, 'base.html', {'nameFinca':nameFinca})

@login_required
def inicio(request):
    user_name = request.session.get('user_name')
    user_role = request.session.get('user_role')

    # Selección de la plantilla base según el rol del usuario
    if user_role == 'Encargado':
        base_template = 'base2.html'
    elif user_role == 'Administrador':
        base_template = 'base.html'
    else:
        base_template = 'base.html'  # O cualquier plantilla predeterminada

    form = forms.FiltroFechaForm(request.GET or None)

    # Obtener los datos según el filtro
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    tipo_registro = request.GET.get('id_tipo_registro')
    agrupacion = request.GET.get('agrupacion')
    
    if tipo_registro == 'Todos':
        fechas_disponibles = ManejoCafe.objects.values_list('fecha', flat=True).distinct().order_by('fecha')
    else:
        fechas_disponibles = ManejoCafe.objects.filter(id_tipo_registro__tipo_registro=tipo_registro).values_list('fecha', flat=True).distinct().order_by('fecha')
    
    fechas_disponibles = [fecha.isoformat() for fecha in fechas_disponibles]
    
    filtro = {}
    if fecha_inicio and fecha_fin:
        fecha_inicio = datetime.fromisoformat(fecha_inicio)
        fecha_fin = datetime.fromisoformat(fecha_fin)
        filtro['fecha__range'] = [fecha_inicio, fecha_fin]
        
    registro_cafe = ManejoCafe.objects.filter(**filtro)
    
    def filtrar(agrupacion):
        if agrupacion == 'dia':
            kilos = registro_cafe.annotate(fecha_agrupada=TruncDay('fecha')).values('fecha_agrupada').annotate(total_peso=Sum('peso'))
        elif agrupacion == 'mes':
            kilos = registro_cafe.annotate(fecha_agrupada=TruncMonth('fecha')).values('fecha_agrupada').annotate(total_peso=Sum('peso'))
        elif agrupacion == 'año':
            kilos = registro_cafe.annotate(fecha_agrupada=TruncYear('fecha')).values('fecha_agrupada').annotate(total_peso=Sum('peso'))
        else:
            kilos = registro_cafe.none()
        return kilos
    
    kilos_json = [
        {
            'fecha': item['fecha_agrupada'].isoformat(),
            'total_peso': item['total_peso']
        }
        for item in filtrar(agrupacion)
    ]
    
    kilos_json = json.dumps(kilos_json)
    
    context = {
        'form': form,
        'kilos': kilos_json,
        'usuario': user_name,
        'fechas_disponibles': fechas_disponibles,
        'base_template': base_template
    }
    return render(request, 'inicio.html', context)

def obtener_fechas(request):
    tipo_registro = request.GET.get('tipo_registro', 'Todos')
    if tipo_registro == 'Todos':
        registros = ManejoCafe.objects.all()
    else:
        registros = ManejoCafe.objects.filter(id_tipo_registro__tipo_registro=tipo_registro)
    fechas = registros.values_list('fecha', flat=True).distinct()
    fechas_formateadas = [fecha.isoformat() for fecha in fechas]
    return JsonResponse({'fechas':fechas_formateadas})