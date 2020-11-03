from django.forms import ModelForm
from .models import TurnosAsignados
from django import forms



class AsignandoTurnos(forms.Form):

    Nombre = forms.CharField(max_length=128)
    Apellido = forms.CharField(max_length=128)
    DNI = forms.IntegerField()
    Descripcion = forms.CharField(widget=forms.Textarea)
    id_turno_libre = forms.IntegerField(label = "Numero de Turno")

class BuscandoDoctor(forms.Form):

    Doctor = forms.CharField(max_length=128, label="Busqueda por nombre de Doctor")