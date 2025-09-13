from django.urls import path
from app_relatorio.views import Relatorio

# Add your views here.
urlpatterns = [
    path("relatorio/", Relatorio),
]
