from django.urls import path
from . import views

urlpatterns = [
    path("login", views.iniciarSesion),
    path("register-admin", views.registrarAdmin),
    path("cambiar-contrasena", views.cambiarContrasena),
    # agregar aqui path para refrescar el token
]
