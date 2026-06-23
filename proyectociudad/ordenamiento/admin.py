from django.contrib import admin
<<<<<<< HEAD
from .models import *

@admin.register(Parroquia)
class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')

@admin.register(Barrio)
class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'parroquia', 'num_parques')

@admin.register(Presidente)
class PresidenteAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'profesion', 'barrio')
=======
from ordenamiento.models import Parroquia

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    search_fields = ('nombre', 'ubicacion')

admin.site.register(Parroquia, ParroquiaAdmin)
>>>>>>> 1d0228d99bf39a117dbc4e2a6bf5261526b7ec2e
