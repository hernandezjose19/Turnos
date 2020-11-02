from django.shortcuts import render
from django.http import HttpResponse
from Doctores import forms
from Doctores.models import TurnosDisponibles


def Inicio(request):
    return render(request, 'home.html')


def TomandoTurnos(request):

    if request.method == "POST":
        formulario = forms.AsignandoTurnos(request.POST)
        if formulario.is_valid():
            formulario.save()
            return render(request, 'vuelta_home.html' )

    else:
        formulario = forms.AsignandoTurnos()
        ctx = {"formu":formulario}
        return render(request, 'agendando_turnos.html', ctx)

def MostrandoTurnos(request):

    turnos = TurnosDisponibles.objects.all()
    ctx = {"turno":turnos}
    return render(request, 'turnos_disponibles.html', ctx)

def Home(request):

    return render(request, 'home.html')