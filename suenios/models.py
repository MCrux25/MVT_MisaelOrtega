from django.db import models
from django.contrib.auth.models import User


# class familiar(models.Model):
#     nombre = models.CharField(max_length=30)
#     suerte = models.IntegerField()
#     nacimiento = models.DateField()

    # def __str__(self):
    #     return self.nombre

class suenios(models.Model):
    titulo = models.CharField(blank = True, max_length=100)
    suenio = models.CharField(max_length=1500)
    pseudonimo = models.CharField(max_length=30)
    fecha = models.DateField()

    def __str__(self):
        return f''' Título:{self.titulo} 
        Fecha:{self.fecha}'''

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta Avatares de media
    image = models.ImageField(upload_to='avatares', null = True, blank = True)

    def __str__(self):
        return f' Avatar de: {self.user}'
