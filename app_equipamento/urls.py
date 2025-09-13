from django.urls import path
from app_equipamento.models.equipamento import Equipamento
from .views import (
    EquipamentoListView,
    EquipamentoCreateView,
    EquipamentoUpdateView,
    EquipamentoDeleteView
)

urlpatterns = [
    path('equipamento/', EquipamentoListView.as_view(), name='equipamento-list'),
    path('equipamentos/create/', EquipamentoCreateView.as_view(), name='equipamento-create'),
    path('equipamentos/<int:id>/update/', EquipamentoUpdateView.as_view(), name='equipamento-update'),
    path('equipamentos/<int:id>/delete/', EquipamentoDeleteView.as_view(), name='equipamento-delete'),
]
