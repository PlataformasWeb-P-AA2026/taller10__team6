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

    def obtener_total_parques(self):
        return sum([b.num_parques for b in self.barrios.all()])

    def obtener_profesiones_presidentes(self):
        return [b.presidente.profesion for b in self.barrios.all() if hasattr(b, 'presidente')]

class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    num_viviendas = models.IntegerField()
    num_parques = models.IntegerField(choices=[(i, str(i)) for i in range(1, 7)])
    num_edificios = models.IntegerField()
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, related_name='barrios')

    def __str__(self):
        return self.nombre

class Presidente(models.Model):
    cedula = models.CharField(max_length=20)
    nickname = models.CharField(max_length=50)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=100)
    barrio = models.OneToOneField(Barrio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname
