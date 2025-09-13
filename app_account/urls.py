from django.urls import path
from app_account.views import (logins, logina)

urlpatterns = [
    path("", logina),
    path("logins/", logins),
]