from django.urls import path
from Doctores import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView




urlpatterns = [
    path('home/', views.Inicio, name="Home"),
    path('login/', LoginView.as_view(template_name = 'login.html'), name = 'Login'),
    path('logout/', LogoutView.as_view(template_name = 'login.html'), name = 'Logout'),
    path('reset-password/', PasswordResetView.as_view(), name="Reset password"),
    path('reset-password-done/', PasswordResetDoneView.as_view(), name="Password done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="Password confirm"),
    path('reset-complete/', PasswordResetCompleteView.as_view(), name="PAssword complete")



]