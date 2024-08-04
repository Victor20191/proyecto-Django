from django import forms
from .models import Tarea

class FormularioTareas(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'importancia']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'importancia': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
