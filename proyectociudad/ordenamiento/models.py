from django.db import models

class Parroquia(models.Model):
    opciones_ubicacion = (
        ('norte', 'Norte'),
        ('sur', 'Sur'),
        ('este', 'Este'),
        ('oeste', 'Oeste'),
    )
    opciones_tipo = (
        ('urbana', 'Urbana'),
        ('rural', 'Rural'),
    )
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=30, choices=opciones_ubicacion)
    tipo = models.CharField(max_length=30, choices=opciones_tipo)

    def __str__(self):
        return "%s" % (self.nombre)
