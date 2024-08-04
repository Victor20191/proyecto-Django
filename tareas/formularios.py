from django.forms import ModelForm
from .models import Tarea

class FormularioTareas(ModelForm):
    class Meta:
        model= Tarea
        fields=['titulo','descripcion','importancia']