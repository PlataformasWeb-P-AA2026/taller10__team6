<<<<<<< HEAD
from django import forms
from .models import Barrio

class BarrioForm(forms.ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'num_viviendas', 'num_parques', 'num_edificios', 'parroquia']
=======
from django.forms import ModelForm
from ordenamiento.models import Parroquia

class ParroquiaForm(ModelForm):
    class Meta:
        model = Parroquia
        fields = ['nombre', 'ubicacion', 'tipo']
>>>>>>> 1d0228d99bf39a117dbc4e2a6bf5261526b7ec2e
