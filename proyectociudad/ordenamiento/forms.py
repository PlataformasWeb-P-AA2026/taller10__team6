from django.forms import ModelForm
from ordenamiento.models import Parroquia, Barrio

class ParroquiaForm(ModelForm):
    class Meta:
        model = Parroquia
        fields = ['nombre', 'ubicacion', 'tipo']

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'num_viviendas', 'num_parques', 'num_edificios', 'parroquia']
