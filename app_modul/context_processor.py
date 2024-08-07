from gestion import models

def name_finca(request):
    nameFinca = models.DatosFinca.objects.all().values('nombre_finca')
    return {'nameFinca':nameFinca}

def user_context(request):
    if request.user.is_authenticated:
        print(f'Usuario autenticado: {request.user.username}')   
        return {
            'logged_in_user': request.user
        }
    return {}
