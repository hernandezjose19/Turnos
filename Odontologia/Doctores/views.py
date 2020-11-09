from django.shortcuts import render
from django.http import HttpResponse
from Doctores import forms
from Doctores.models import TurnosDisponibles, TurnosAsignados
import sqlite3
from django.contrib.auth.decorators import login_required


#Esta les muestra a los doctores todos los turnos que se han registrado


@login_required
def Inicio(request):

    conn = sqlite3.connect("db.sqlite3") 
    cursor = conn.cursor()
    consulta = ("SELECT d.Fecha, d.Hora, d.Doctor, j.Nombre, j.Apellido, j.DNI, j.Descripcion FROM Doctores_turnosasignados AS j JOIN Doctores_turnosdisponibles AS d ON j.ID_Turno_Disponible == d.id")
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    ctx = {"resultado":resultado}
    return render(request, 'home_login.html', ctx)


#Aca los pacientes se asignan sus turnos

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

            )  
            
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

#Aca muestra todos los turnos disponibles

def MostrandoTurnos(request):


    conex = sqlite3.connect("db.sqlite3")
    cursor = conex.cursor()
    sql = (
        "SELECT CASE WHEN j.Fecha = c.Apellido THEN j.id ELSE j.id END  AS 'Numero de turno', CASE WHEN j.Fecha = c.Apellido THEN j.Fecha ELSE Fecha END  AS Fecha, CASE WHEN j.Fecha = c.Apellido THEN j.Hora ELSE Hora END  AS Hora, CASE WHEN j.Fecha = c.Apellido THEN j.Doctor ELSE Doctor END  AS Doctor, CASE WHEN j.Fecha = c.Apellido THEN j.Especialidad ELSE Especialidad END  AS Especialidad, CASE WHEN j.id = c.ID_Turno_Disponible THEN 'Ocupado' ELSE 'Disponible' END As Estado FROM Doctores_turnosdisponibles AS j LEFT JOIN Doctores_turnosasignados AS c ON j.id = c.ID_Turno_Disponible"
    )
    cursor.execute(sql)
    turnos = cursor.fetchall()
    ctx = {"turno":turnos}
    return render(request, 'turnos_disponibles.html', ctx)


def Home(request):

    return render(request, 'home.html')


#Esta vista permite a los doctores filtrar las busquedas por nombre de Doctor

@login_required
def Busqueda_avanzada(request):

    if request.method == "POST":

        formu = forms.BuscandoDoctor(request.POST)
        if formu.is_valid():

            conex = sqlite3.connect("db.sqlite3")
            cursor = conex.cursor()
            nombre_doctor = str(formu.cleaned_data["Doctor"]).title()
            sql = ("SELECT d.Fecha, d.Hora, d.Doctor, j.Nombre, j.Apellido, j.DNI, j.Descripcion FROM Doctores_turnosasignados AS j JOIN Doctores_turnosdisponibles AS d ON j.ID_Turno_Disponible == d.id WHERE d.Doctor == ?", (nombre_doctor,))
            cursor.execute(*sql)
            resultado = cursor.fetchall()
            conex.close()
            ctx = {"resultado":resultado}
            return render(request, 'resultado_busqueda.html', ctx)

    else:
        formu = forms.BuscandoDoctor()
        ctx = {"resultado": formu}
        return render(request, 'busqueda.html', ctx)



#Esta vissta muestra los turnos a los pacientes una vez ingresado su dni

def Turnos_pacientes(request):

    
    if request.method == "POST":
        
        formu = forms.TurnosPaciente(request.POST)
        
        if formu.is_valid():
        
            dni = formu.cleaned_data['DNI']
            conex = sqlite3.connect("db.sqlite3")
            cursor = conex.cursor()
            consulta = ("SELECT * FROM Doctores_turnosasignados AS c JOIN Doctores_turnosdisponibles AS j ON c.ID_Turno_Disponible = j.id WHERE c.DNI = ?", (dni,))
            cursor.execute(*consulta)
            resultado = cursor.fetchall()
            conex.close()
            ctx = {"datos_turno_paciente":resultado}
            return render(request, 'turno_paciente.html', ctx)

    else:

        formu = forms.TurnosPaciente()
        ctx = {"formu":formu}
        return render(request, 'dni_paciente.html', ctx )



#Los pacientes cambian sus turnos colocando el id del turno al cual quieren cambiar y seguido  su id de turno actual

def Cambiando_turnos_pacientes(request):


    if request.method == "POST":

        formu = forms.CambiandoTurnos(request.POST)
        if formu.is_valid():

            id_nuevo = formu.cleaned_data["ID_turno_nuevo"]
            id_actual = formu.cleaned_data["ID_turno_actual"]
            conex = sqlite3.connect("db.sqlite3")
            cursor = conex.cursor()
            consulta = ("UPDATE Doctores_turnosasignados SET ID_Turno_Disponible = ? WHERE ID_Turno_Disponible == (?)", (id_nuevo, id_actual) )
            cursor.execute(*consulta)
            conex.commit()
            conex.close()
            return render(request, 'turno_cambiado.html')

    else:

        formu = forms.CambiandoTurnos()
        ctx = {"formu":formu}
        return render(request, 'cambiando_turnos.html', ctx)


def Cancelando_turno(request):

    if request.method == "POST":

        formu = forms.CancelandoTurnos(request.POST)
        if formu.is_valid():

            conex = sqlite3.connect("db.sqlite3")
            cursor = conex.cursor()
            id_turno_actual = formu.cleaned_data['ID_Turno_actual']
            sql = ('DELETE FROM Doctores_turnosasignados WHERE ID_Turno_Disponible = ?', (id_turno_actual,))
            cursor.execute(*sql)
            conex.commit()
            conex.close()
            return HttpResponse("Turno cancelado con exito")

    else:

        formu = forms.CancelandoTurnos()
        ctx = {"formu": formu}
        return render(request, 'cancelando_turnos.html', ctx)

