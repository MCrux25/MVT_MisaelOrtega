from django.shortcuts import render
from familia.models import *


def familia (request):
    integrantes = familiar.objects.all()
    return render(request, 'familia.html', {'familiar': integrantes})

def casa(request):
    return render (request,'jefe.html')

def mascotas(request):
    return render (request,'mascotas.html')

def otra(request):
    if request.method == "POST":
        sueño = sueños (sueño = request.POST['sueño'], pseudonimo = request.POST['pseudonimo'], fecha = request.POST['fecha'])
        sueño.save()
        return render (request, 'casa.html', {'sueño' : sueño })
    return render (request, 'otra.html')
