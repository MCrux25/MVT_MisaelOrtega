from django.shortcuts import render, redirect
from suenios.models import *

from django.contrib.auth.forms import *
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from .forms import *
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

def aboutme(request):
    data = {'name': 'Julia', 'age': '28', 'zodiac':'piscis'}
    return render (request, "acerca.html", data)

@login_required
def create_suenio(request):
    if request.method == "POST":
        zuenio = suenios (titulo = request.POST['titulo'] ,suenio = request.POST['suenio'], pseudonimo = request.POST['pseudonimo'], fecha = request.POST['fecha'])
        zuenio.save()
        zuenio = suenios.objects.all()
        return render (request, "read_suenio.html", {'suenios':zuenio})
    return render (request, 'create_suenio.html')

@login_required
def read_suenio(request):
    zuenio = suenios.objects.all()
    return render (request, "read_suenio.html", {'suenios':zuenio})

@login_required
def suenioView(request,zuenio_pseudonimo):  
    zuenio = suenios.objects.get(pseudonimo =  zuenio_pseudonimo)
    return render(request, 'suenio.html', {'suenios':zuenio})

@login_required
def update_suenio(request,zuenio_pseudonimo):
    zuenio = suenios.objects.get(pseudonimo =  zuenio_pseudonimo)
    if request.method == "POST":
        form = EditZuenios (request.POST)
        if form.is_valid():
            info = form.cleaned_data
            zuenio.titulo = info ['titulo']
            zuenio.suenio = info ['sueño']
            zuenio.pseudonimo = info ['pseudonimo']
            zuenio.fecha = info ['fecha']
            zuenio.save()
        return redirect ('/suenios/read_suenio/')
    else:
        form = EditZuenios (initial = {'titulo': zuenio.titulo,'sueño': zuenio.suenio, 'pseudonimo': zuenio.pseudonimo, 'fecha': zuenio.fecha})
    return render(request, "update_suenio.html", {"form": form})

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
                return render (request, "inicio.html")
            else:
                return render (request, "login.html", {'form':form})
        else:
            return render (request, "login.html", {'form':form})
    form = AuthenticationForm()
    return render (request, "login.html", {'form':form})

def registro(request):
    form = UserRegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect ("/suenios/login")
        else:
            return render(request, "registro.html",{'form':form})
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
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'perfil.html', {'avatar': avatar})
        else:
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'perfil.html', {'form':form, 'avatar': avatar})
    else:
        form = UserEditForm(initial={'email': usuario.email, 'username': usuario.username, 'first_name': usuario.first_name, 'last_name': usuario.last_name })
    return render(request, 'editarPerfil.html', {'form': form, 'usuario': usuario})

@login_required
def changepass(request):
    usuario = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, 'inicio.html')
    else:
        form = ChangePasswordForm(user = request.user)
    return render(request, 'changepass.html', {'form': form, 'usuario': usuario})

@login_required
def perfilView(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    print(usuario)
    return render(request, 'perfil.html', {'form':user_basic_info})

@login_required
def AgregarAvatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, 'perfil.html', {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarFormulario()
        except:
            form = AvatarFormulario()
    return render(request, 'AgregarAvatar.html', {'form': form})

