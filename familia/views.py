from django.shortcuts import render

from familia.models import familiar

def familia (request):
    integrantes = familiar.objects.all()
    return render(request, 'familia.html', {'familiar': integrantes})

def casa(request):
    return render (request,'jefe.html')

def mascotas(request):
    return render (request,'mascotas.html')

def otra(request):
    return render (request,'otra.html')
