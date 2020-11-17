from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required
from Doctores import views


urlpatterns = [
    
    path('home', views.home, name="Home"), #Este home es el principal de la pagina
    path('acceso/home/', views.inicio, name="Home Login"), #Home para los doctores logueados
    path('login/', LoginView.as_view(template_name = 'login.html'), name = "Login"),
    path('logout/', LogoutView.as_view(template_name = 'login.html'), name = "Logout"),
    path('agendando-turnos/', views.tomando_turnos, name="Turnos"),
    path('turnos/disponibles/', views.mostrando_turnos, name="Turnos libres"),
    path('acceso/home/busqueda/', login_required(views.busqueda_avanzada), name = "Busqueda avanzada"),
    path('mis-turnos/', views.turnos_pacientes, name = "Turnos_de_los_pacientes"),
    path('mis-turnos/cambiando-turno/', views.cambiando_turnos_pacientes, name= "Cambio_turnos_pacientes"),
    path('mis-turnos/canclar-turno/', views.cancelando_turno, name="Cancelando_turnos"),
    path('reset-password/',views.PasswordResetView.as_view(), name = "Reseteo"),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name= 'password_cambio_enviado.html'), name = "Enviando_mail"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='reset_passwords_new.html'),  name="Confirmando_reseteo"),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name = 'reseteo_completado.html'), name = "Reseteo_completado")


]



