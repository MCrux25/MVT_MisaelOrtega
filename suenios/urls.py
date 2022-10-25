from django.urls import path
from suenios.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('', casa),
    #path('familia/', familia),
    #path('mascotas/', mascotas),
    #path('otra/', otra),
    path('read_suenio/', read_suenio),
    path('create_suenio/', create_suenio),
    path('update_suenio/<zuenio_pseudonimo>', update_suenio),
    path('delete_suenio/<zuenio_pseudonimo>', delete_suenio),
    path('suenio/<zuenio_pseudonimo>', suenioView),
    path('login/', login_request),
    path('registro/', registro),
    path('logout/', LogoutView.as_view (template_name = "acerca.html"), name = "Logout"),
    path('perfil/', perfilView),
    path('perfil/editarPerfil/', editar_perfil),
    path('perfil/changepass/', changepass),
]