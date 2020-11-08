from django.urls import path
from Doctores import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required



urlpatterns = [
    
    path('home', views.Home, name="Home"), #Este home, sera el home principal, tendra redireccionamientos a reserva de turnos y acceso doctores(es decir, al login de doctores)
    path('acceso/home/', views.Inicio, name="Home Login"), #ESte Home es luego de que los doctores se loguean, es decir, seria el home de doctores y veran los turnos asignados
    path('login/', LoginView.as_view(template_name = 'login.html'), name = 'Login'),
    path('logout/', LogoutView.as_view(template_name = 'login.html'), name = 'Logout'),
    path('reset-password/', PasswordResetView.as_view(), name="Reset password"),
    path('reset-password-done/', PasswordResetDoneView.as_view(), name="Reset done"),
    path('reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="Password confirm"),
    path('reset-complete/', PasswordResetCompleteView.as_view(), name="Password complete"),
    path('turnos/', views.TomandoTurnos, name="Turnos"),
    path('turnos/disponibles/', views.MostrandoTurnos, name="Turnos libres"),
    path('acceso/home/busqueda/', login_required(views.Busqueda_avanzada), name = "Busqueda avanzada"),
    path('mis-turnos/', views.Turnos_pacientes, name = "Turnos_de_los_pacientes"),
    path("mis-turnos/cambiando-turno/", views.Cambiando_turnos_pacientes, name= "Cambio_turnos_pacientes")



]



