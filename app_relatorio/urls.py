from django.urls import path
from app_relatorio.views import relatorio

# Add your views here.
urlpatterns = [
    path("relatorio/", relatorio),
]
