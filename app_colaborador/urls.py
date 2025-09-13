from django.urls import path
from app_colaborador.models.colaborador import Colaborador
from .views import (
    ColaboradorListView,
    ColaboradorCreateView,
    ColaboradorUpdateView,
    ColaboradorDeleteView
)

urlpatterns = [
    path('colaborador/', ColaboradorListView.as_view(), name='colaborador-list'),
    path('colaboradores/create/', ColaboradorCreateView.as_view(), name='colaborador-create'),
    path('colaboradores/<int:id>/update/', ColaboradorUpdateView.as_view(), name='colaborador-update'),
    path('colaboradores/<int:id>/delete/', ColaboradorDeleteView.as_view(), name='colaborador-delete'),
]