from gestion import models

def name_finca(request):
    nameFinca = models.DatosFinca.objects.all().values('nombre_finca')
    return {'nameFinca':nameFinca}