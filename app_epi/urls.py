from django.urls import path
from app_epi.views import (
    logina,
    inicio,
    sobre,
    Colaboradores,
    Equipamentos,
    Usuarios,
    Emprestimos,
    logins,
)

urlpatterns = [
    path("", logina),
    path("inicio/", inicio),
    path("sobre/", sobre),
    path("colaboradores/", Colaboradores),
    path("equipamentos/", Equipamentos),
    path("usuarios/", Usuarios),
    path("emprestimos/", Emprestimos),
    path("logins/", logins),
]
