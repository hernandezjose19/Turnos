from django.db import models


class TurnosDisponibles(models.Model):

    Fecha = models.DateField()
    Hora = models.TimeField()
    Doctor = models.CharField(max_length=128)
    Especialidad = models.CharField(max_length=128)


class TurnosAsignados(models.Model):

    Nombre = models.CharField(max_length=128)
    Apellido = models.CharField(max_length=128)
    DNI = models.IntegerField()
    Descripcion = models.TextField(max_length=65535)
    ID_Turno_Disponible = models.IntegerField(unique=True)

    def __str__(self):

        return self.Doctor


