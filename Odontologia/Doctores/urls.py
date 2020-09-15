from django.urls import path
from Doctores import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('home/', views.Inicio, name="Home"),
    path('login/', LoginView.as_view(template_name = 'login.html'), name = 'Login'),
    path('logout/', LogoutView.as_view(template_name = 'login.html'), name = 'Logout')

]