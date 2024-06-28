from django.shortcuts import render

# Create your views here.
def usuario(request):
    data = request.get
    print (data)
    return render(request, 'crear_usuario.html')