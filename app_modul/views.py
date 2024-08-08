from django.shortcuts import render
from regfield.decoractors import login_required
from gestion.models import ManejoCafe, DatosFinca
import json
from django.db.models import Sum
from . import forms
from django.db.models.functions import TruncDay, TruncMonth, TruncYear, TruncWeek
from datetime import datetime


# Create your views here.
def base(request):
    nameFinca = DatosFinca.objects.all().values('nombre_finca')
    return render(request, 'base.html', {'nameFinca':nameFinca})

@login_required
def inicio(request):
    user_name = request.session.get('user_name')
    form = forms.FiltroFechaForm(request.GET or None)
    
    # Obtener fechas disponibles para el filtrado
    fechas_disponibles = ManejoCafe.objects.values_list('fecha', flat=True).distinct().order_by('fecha')
    fechas_disponibles = [fecha.isoformat() for fecha in fechas_disponibles]

    # Obtener los datos según el filtro
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    tipo_registro = request.GET.get('id_tipo_registro')
    agrupacion = request.GET.get('agrupacion', 'dia')  # Valor predeterminado
    
    filtro = {}
    if fecha_inicio and fecha_fin:
        fecha_inicio = datetime.fromisoformat(fecha_inicio)
        fecha_fin = datetime.fromisoformat(fecha_fin)
        filtro['fecha__range'] = [fecha_inicio, fecha_fin]
    if tipo_registro:
        filtro['tipo_registro'] = tipo_registro
    
    # Aplicar filtro y agrupar
    queryset = ManejoCafe.objects.filter(**filtro)

    if agrupacion == 'dia':
        queryset = queryset.annotate(fecha_agrupada=TruncDay('fecha'))
    elif agrupacion == 'semana':
        queryset = queryset.annotate(fecha_agrupada=TruncWeek('fecha'))
    elif agrupacion == 'mes':
        queryset = queryset.annotate(fecha_agrupada=TruncMonth('fecha'))
    elif agrupacion == 'año':
        queryset = queryset.annotate(fecha_agrupada=TruncYear('fecha'))
    
    kilos = queryset.values('fecha').annotate(total_peso=Sum('peso'))
    
    # Convertir fechas a formato ISO para el frontend
    kilos_json = [
        {
            'fecha': item['fecha'].isoformat(),
            'total_peso': item['total_peso']
        }
        for item in kilos
    ]
    
    kilos_json = json.dumps(kilos_json)  # Serializa el queryset a JSON
    
    context = {
        'form': form,
        'kilos': kilos_json,
        'usuario': user_name,
        'fechas_disponibles': fechas_disponibles
    }
    
    print(fechas_disponibles)
    print(filtro)
    print(kilos)
    
    return render(request, 'inicio.html', context)






