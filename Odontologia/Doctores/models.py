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
    ID_Turno_Disponible = models.IntegerField(unique=True, null= True)#este campo debe ser unique = "True" para que no se repitan los turnos

"""Estos modelos de Profesor y Materias fueron solo de prueba, no van en la aplicacion"""

class Profesor(models.Model):


    Nombre = models.CharField(max_length=128)
    Apellido = models.CharField(max_length=128)
    DNI = models.IntegerField()

class Materia(models.Model):


    Nombre = models.CharField(max_length=128)
    Docente = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True)