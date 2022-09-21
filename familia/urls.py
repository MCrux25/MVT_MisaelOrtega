from django.urls import path
from familia.views import *

urlpatterns = [
    path('', casa),
    path('familia/', familia),
    path('mascotas/', mascotas),
    path('otra/', otra),
    path('read_suenio/', read_suenio),
    path('create_suenio/', create_suenio),
    path('delete_suenio/<zuenio_pseudonimo>', delete_suenio),
]