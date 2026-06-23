from django.contrib import admin
from ordenamiento.models import Parroquia, Barrio, Presidente

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    search_fields = ('nombre', 'ubicacion')
admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'parroquia', 'num_parques')
admin.site.register(Barrio, BarrioAdmin)

class PresidenteAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'profesion', 'barrio')
admin.site.register(Presidente, PresidenteAdmin)
