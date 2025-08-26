from django.urls import path
from app_epi.views import inicio, sobre

urlpatterns = [
    path('', inicio),
    path('sobre/', sobre),
]