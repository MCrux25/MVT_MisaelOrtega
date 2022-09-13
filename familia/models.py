from django.db import models

class familiar(models.Model):
    nombre = models.CharField(max_length=30)
    suerte = models.IntegerField()
    nacimiento = models.DateField()

    def __str__(self):
        return self.nombre, self.suerte