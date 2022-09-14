from django.urls import path
from familia.views import *

urlpatterns = [
    path('', casa),
    path('familia/', familia),
    path('mascotas/', mascotas),
    path('otra/', otra),
]