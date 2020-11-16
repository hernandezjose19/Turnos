
from django.urls import path
from Doctores import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required



urlpatterns = [
    
    path('home', views.Home, name="Home"), #Este home, sera el home principal, tendra redireccionamientos a reserva de turnos y acceso doctores(es decir, al login de doctores)
    path('acceso/home/', views.Inicio, name="Home Login"), #ESte Home es luego de que los doctores se loguean, es decir, seria el home de doctores y veran los turnos asignados
    path('login/', LoginView.as_view(template_name = 'login.html'), name = "Login"),
    path('logout/', LogoutView.as_view(template_name = 'login.html'), name = "Logout"),
    path('agendando-turnos/', views.TomandoTurnos, name="Turnos"),
    path('turnos/disponibles/', views.MostrandoTurnos, name="Turnos libres"),
    path('acceso/home/busqueda/', login_required(views.Busqueda_avanzada), name = "Busqueda avanzada"),
    path('mis-turnos/', views.Turnos_pacientes, name = "Turnos_de_los_pacientes"),
    path('mis-turnos/cambiando-turno/', views.Cambiando_turnos_pacientes, name= "Cambio_turnos_pacientes"),
    path('mis-turnos/canclar-turno/', views.Cancelando_turno, name="Cancelando_turnos"),
    path('reset-password/',views.PasswordResetView.as_view(), name = "Reseteo"),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name= 'password_cambio_enviado.html'), name = "Enviando_mail"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='reset_passwords_new.html'),  name="Confirmando_reseteo"),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name = 'reseteo_completado.html'), name = "Reseteo_completado")


]



