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

    Doctor = forms.CharField(max_length=128, label="Nombre y Apellido del Doctor")

class TurnosPaciente(forms.Form):

    DNI = forms.IntegerField(label = "Por favor introduzca su DNI")


class CambiandoTurnos(forms.Form):

    ID_turno_nuevo = forms.IntegerField(label="ID de Turno nuevo")
    ID_turno_actual = forms.IntegerField(label="ID de turno actual")
    

class CancelandoTurnos(forms.Form):


    ID_Turno_actual = forms.IntegerField(label = "ID de turno a cancelar")


class ResetPasswordForm(forms.Form):

    username = forms.CharField(label="Nombre de usuario")