from django.shortcuts import render

from familia.models import familiar

def familia (request):
    integrantes = familiar.objects.all()
    return render(request, 'familia.html', {'familiar': integrantes})
