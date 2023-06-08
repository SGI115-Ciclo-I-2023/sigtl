from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("login", views.iniciarSesion),
    path("register-admin", views.registrarAdmin),
    path("cambiar-contrasena", views.cambiarContrasena),
    # agregar aqui path para refrescar el token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
