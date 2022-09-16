from django.db import models

class familiar(models.Model):
    nombre = models.CharField(max_length=30)
    suerte = models.IntegerField()
    nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class sueños(models.Model):
    sueño = models.CharField(max_length=100)
    pseudonimo = models.CharField(max_length=30)
    fecha = models.DateField()