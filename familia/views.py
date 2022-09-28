from django.shortcuts import render, redirect
from familia.models import *

from django.contrib.auth.forms import *
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from .forms import ChangePasswordForm, UserRegisterForm, UserEditForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


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
    form = UserRegisterForm(request.POST)
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        if form.is_valid():
            #username = form.cleaned_data['username']
            form.save()
            return redirect ("/familia/login")
        else:
            return render(request, "registro.html",{'form':form})
    #form = UserCreationForm()
    form = UserRegisterForm()
    return render (request, "registro.html", {'form':form})

@login_required
def editar_perfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render (request, "index.html")
        else:
            return render(request, "index.html",{'form':form})
    else:
        form = UserEditForm(initial= {'email':usuario.email, 'username': usuario.username, 'first_name': usuario.first_name, 'last_name': usuario.last_name}) 
        return render(request, "editarperfil.html",{'form':form, 'usuario':usuario})


@login_required
def changepass(request):
    usuario = request.user
    if request.method == 'POST':
        #form = PasswordChangeForm(data = request.POST, user = usuario)
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, 'home.html')
    else:
        #form = PasswordChangeForm(request.user)
        form = ChangePasswordForm(user = request.user)
    return render(request, 'changepass.html', {'form': form, 'usuario': usuario})

@login_required
def perfilView(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    print(usuario)
    return render(request, 'perfil.html', {'form':user_basic_info})

@login_required
def perfilView(request):
    return render(request, 'perfil.html')

