from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from gestion.models import ManejoCafe, DatosFinca
import json
from django.db.models import Sum

# Create your views here.
def base(request):
    nameFinca = DatosFinca.objects.all().values('nombre_finca')
    return render(request, 'base.html', {'nameFinca':nameFinca})

@login_required
def inicio(request):
    kilos = ManejoCafe.objects.all().values('fecha').annotate(total_peso=Sum('peso'))
    
    for item in kilos:
        item['fecha'] = item['fecha'].isoformat()
    kilos_json = json.dumps(list(kilos))  # Serializa el queryset a JSON
    context = {
        'kilos': kilos_json
    }
    return render(request, 'inicio.html', context)

@login_required
def finca(request):
    return render(request, 'datos_finca.html')