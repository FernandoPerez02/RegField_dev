from django.shortcuts import render, redirect
from regfield.decoractors import login_required
from gestion.models import ManejoCafe, DatosFinca
import json
from django.db.models import Sum


# Create your views here.
def base(request):
    nameFinca = DatosFinca.objects.all().values('nombre_finca')
    return render(request, 'base.html', {'nameFinca':nameFinca})

@login_required
def inicio(request):
    user_name = request.session.get('user_name')    
    kilos = ManejoCafe.objects.all().values('fecha').annotate(total_peso=Sum('peso'))
    
    for item in kilos:
        item['fecha'] = item['fecha'].isoformat()
    kilos_json = json.dumps(list(kilos))  # Serializa el queryset a JSON
    context = {
        'kilos': kilos_json,
        'usuario': user_name
    }
    
    return render(request, 'inicio.html', context)


