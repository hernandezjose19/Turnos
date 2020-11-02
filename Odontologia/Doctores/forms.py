from django.forms import ModelForm
from .models import TurnosAsignados


class AsignandoTurnos(ModelForm):
    
    class Meta:

        model = TurnosAsignados
        fields = ('Nombre', 'Apellido', 'DNI', 'Descripcion', 'ID_Turno_Disponible')