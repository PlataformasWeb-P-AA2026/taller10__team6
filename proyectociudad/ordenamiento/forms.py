from django.forms import ModelForm
from ordenamiento.models import Parroquia

class ParroquiaForm(ModelForm):
    class Meta:
        model = Parroquia
        fields = ['nombre', 'ubicacion', 'tipo']
