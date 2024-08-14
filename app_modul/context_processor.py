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

def base_template(request):
    user_role = request.session.get('user_role')

    if user_role == 'Encargado':
        base_template = 'base2.html'
    elif user_role == 'Administrador':
        base_template = 'base.html'
    else:
        base_template = 'base.html'  # O cualquier plantilla predeterminada

    return {'base_template': base_template}
