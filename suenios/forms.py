from operator import imod
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import *

class UserRegisterForm(UserCreationForm): #no sube foto de perfil, no permite creación de usuarios
    first_name = forms.CharField(label = "Nombre:")
    last_name = forms.CharField(label = "Apellidos(s):")
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir contraseña", widget= forms.PasswordInput)
    #image = forms.ImageField(label = "Foto de perfil:") 

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name','last_name']
        help_text = {k: "" for k in fields}

class UserEditForm(UserChangeForm): ##No modifica datos de usuario (nombre, apellido y avatar)
    username = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder': 'email'}))
    first_name = forms.CharField(label = "Nombre:",widget= forms.TextInput(attrs={'placeholder': 'first_name'}))
    last_name = forms.CharField(label = "Apellido(s):",widget= forms.TextInput(attrs={'placeholder': 'last_name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    #image = forms.ImageField(label = "Foto de perfil:")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        help_text = {k: "" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="", widget= forms.PasswordInput(attrs={'placeholder': "Old Password", }))
    new_password1 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder': "New password"}))
    new_password2 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder': "Confirm new password"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}

class EditZuenios(forms.Form):
    titulo = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Título'}))
    sueño = forms.CharField(widget= forms.Textarea(attrs={'placeholder': 'Sueño',"rows":5}))
    pseudonimo = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Pseudonimo'}))
    fecha = forms.DateField(widget= forms.TextInput(attrs={'placeholder': 'Fecha'}))

class AvatarFormulario(forms.Form):
    avatar = forms.ImageField()