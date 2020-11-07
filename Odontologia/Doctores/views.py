from django.shortcuts import render
from django.http import HttpResponse
from Doctores import forms
from Doctores.models import TurnosDisponibles, TurnosAsignados
import sqlite3
from django.contrib.auth.decorators import login_required


@login_required
def Inicio(request):

    conn = sqlite3.connect("db.sqlite3") #ESta vista devuelve TODOS los turnos asignados a los doctores, en la url: doctores/login/home/
    cursor = conn.cursor()
    consulta = ("SELECT d.Fecha, d.Hora, d.Doctor, j.Nombre, j.Apellido, j.DNI, j.Descripcion FROM Doctores_turnosasignados AS j JOIN Doctores_turnosdisponibles AS d ON j.ID_Turno_Disponible == d.id")
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    ctx = {"resultado":resultado}
    return render(request, 'home_login.html', ctx)


def TomandoTurnos(request):

    if request.method == "POST":

        formu = forms.AsignandoTurnos(request.POST)
        if formu.is_valid():

            TurnosAsignados.objects.create(
                Nombre = str(formu.cleaned_data["Nombre"]).title(),
                Apellido = str(formu.cleaned_data["Apellido"]).title(),
                DNI = formu.cleaned_data["DNI"],
                Descripcion = formu.cleaned_data["Descripcion"],
                ID_Turno_Disponible = formu.cleaned_data["id_turno_libre"]

            )  #Esta vista se encarga de agendar los turnos(parte de arriba) y mostrar informacion acerca del turno una vez asignado(parte de abajo)url:doctores/turnos/ y retorna los datos del turno
            
            a = formu.cleaned_data["id_turno_libre"]
            conn = sqlite3.connect("db.sqlite3")
            cursor = conn.cursor()
            otra = ("SELECT d.Fecha, d.Hora, d.Especialidad, d.Doctor FROM Doctores_turnosasignados JOIN Doctores_turnosdisponibles AS d ON Doctores_turnosasignados.ID_Turno_Disponible == d.id WHERE Doctores_turnosasignados.ID_Turno_Disponible == ?", (a,))
            cursor.execute(*otra)
            consul = cursor.fetchall()
            consulta = {"consulta":consul}
            return render(request, 'vuelta_home.html', consulta)

    else:
        formulario = forms.AsignandoTurnos()
        ctx = {"formu":formulario}
        return render(request, 'agendando_turnos.html', ctx)


def MostrandoTurnos(request):

#Esta vista se encarga de mostrar los turnos disponibles en la url: doctores/turnos/disponibles/

    turnos = TurnosDisponibles.objects.all()
    ctx = {"turno":turnos}
    return render(request, 'turnos_disponibles.html', ctx)


def Home(request):

    return render(request, 'home.html')


@login_required
def Busqueda_avanzada(request):

    if request.method == "POST":

        formu = forms.BuscandoDoctor(request.POST)
        if formu.is_valid():

            conn = sqlite3.connect("db.sqlite3")
            cursor = conn.cursor()
            nombre_doctor = str(formu.cleaned_data["Doctor"]).title()
            sql = ("SELECT d.Fecha, d.Hora, d.Doctor, j.Nombre, j.Apellido, j.DNI, j.Descripcion FROM Doctores_turnosasignados AS j JOIN Doctores_turnosdisponibles AS d ON j.ID_Turno_Disponible == d.id WHERE d.Doctor == ?", (nombre_doctor,))
            cursor.execute(*sql)
            resultado = cursor.fetchall()
            ctx = {"resultado":resultado}
            return render(request, 'resultado_busqueda.html', ctx)

    else:
        formu = forms.BuscandoDoctor()
        ctx = {"resultado": formu}
        return render(request, 'busqueda.html', ctx)


def Turnos_pacientes(request):
    if request.method == "POST":
        
        formu = forms.TurnosPaciente(request.POST)
        
        if formu.is_valid():
        
            dni = formu.cleaned_data['DNI']
            connex = sqlite3.connect("db.sqlite3")
            cursor = connex.cursor()
            consulta = ("SELECT * FROM Doctores_turnosasignados WHERE DNI == ?", (dni,))
            cursor.execute(*consulta)
            resultado = cursor.fetchall()
            ctx = {"datos_turno_paciente":resultado}
            return render(request, 'turno_paciente.html', ctx)

    else:

        formu = forms.TurnosPaciente()
        ctx = {"formu":formu}
        return render(request, 'dni_paciente.html', ctx )


def Cambiando_turnos_pacientes(request):


    if request.method == "POST":

        formu = forms.CambiandoTurnos(request.POST)
        if formu.is_valid():

            id_nuevo = formu.cleaned_data["ID_turno_nuevo"]
            id_actual = formu.cleaned_data["ID_turno_actual"]
            connec = sqlite3.connect("db.sqlite3")
            cursor = connec.cursor()
            consulta = ("UPDATE Doctores_turnosasignados SET ID_Turno_Disponible = ? WHERE ID_Turno_Disponible == (?)", (id_nuevo, id_actual) )
            cursor.execute(*consulta)
            connec.commit()
            return render(request, 'turno_cambiado.html')

    else:

        formu = forms.CambiandoTurnos()
        ctx = {"formu":formu}
        return render(request, 'cambiando_turnos.html', ctx)







