from django.urls import path
from app_epi.views import (inicio, sobre)
from app_account.views import logina, logins

urlpatterns = [
    path("", logina),
    path("inicio/", inicio),
    path("sobre/", sobre),
    path("logins/", logins),
]
