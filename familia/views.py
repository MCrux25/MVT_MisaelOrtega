from django.shortcuts import render
from familia.models import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm

from django.contrib.auth.decorators import login_required

@login_required
def familia (request):
    integrantes = familiar.objects.all()
    return render(request, 'familia.html', {'familiar': integrantes})

def casa(request):
    return render (request,'jefe.html')

def mascotas(request):
    return render (request,'mascotas.html')


# def otra(request):
#     if request.method == "POST":
#         zuenio = suenios (suenio = request.POST['suenio'], pseudonimo = request.POST['pseudonimo'], fecha = request.POST['fecha'])
#         zuenio.save()
#         return render (request, 'jefe.html')
#     return render (request, 'otra.html')

@login_required
def create_suenio(request):
    if request.method == "POST":
        zuenio = suenios (suenio = request.POST['suenio'], pseudonimo = request.POST['pseudonimo'], fecha = request.POST['fecha'])
        zuenio.save()
        zuenio = suenios.objects.all()
        return render (request, "read_suenio.html", {'suenios':zuenio})
    return render (request, 'create_suenio.html')

@login_required
def read_suenio(request):
    zuenio = suenios.objects.all()
    return render (request, "read_suenio.html", {'suenios':zuenio})

@login_required
def delete_suenio(request, zuenio_pseudonimo):
    zuenio = suenios.objects.get(pseudonimo =  zuenio_pseudonimo)
    zuenio.delete()

    zuenio = suenios.objects.all()    
    return render(request, "read_suenio.html", {"suenios": zuenio})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user, password = pwd)

            if user is not None:
                login(request,user)
                return render (request, "index.html")
            else:
                return render (request, "login.html", {'form':form})
        else:
            return render (request, "login.html", {'form':form})
    form = AuthenticationForm()
    return render (request, "login.html", {'form':form})

def registro(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #username = form.cleaned_data['username']
            form.save()
            return render (request, "login.html")
    #form = UserCreationForm()
    form = UserRegisterForm()
    return render (request, "registro.html", {'form':form})