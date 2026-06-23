from django.contrib import admin
from ordenamiento.models import Parroquia

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    search_fields = ('nombre', 'ubicacion')

admin.site.register(Parroquia, ParroquiaAdmin)
