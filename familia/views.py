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
        zuenio = suenios (suenio = request.POST['suenio'], pseudonimo = request.POST['pseudonimo'], fecha = request.POST['fecha'])
        zuenio.save()
        return render (request, 'jefe.html')
    return render (request, 'otra.html')

def create_suenio(request):
    if request.method == "POST":
        zuenio = suenios (suenio = request.POST['suenio'], pseudonimo = request.POST['pseudonimo'], fecha = request.POST['fecha'])
        zuenio.save()
        zuenio = suenios.objects.all()
        return render (request, "read_suenio.html", {'suenios':zuenio})
    return render (request, 'create_suenio.html')

def read_suenio(request):
    zuenio = suenios.objects.all()
    return render (request, "read_suenio.html", {'suenios':zuenio})

def delete_suenio(request, zuenio_pseudonimo):
    zuenio = suenios.objects.get(pseudonimo =  zuenio_pseudonimo)
    zuenio.delete()

    zuenio = suenios.objects.all()    
    return render(request, "read_suenio.html", {"suenios": zuenio})
