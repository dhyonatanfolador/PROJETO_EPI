from django.urls import path
from .views import (
    EquipamentoListView,
    EquipamentoCreateView,
    EquipamentoUpdateView,
    EquipamentoDeleteView,
    Equipamento
)

urlpatterns = [
    path('equipamento/', Equipamento, name='equipamento'),
    path('equipamentos/', EquipamentoListView.as_view(), name='equipamento-list'),
    path('equipamentos/create/', EquipamentoCreateView.as_view(), name='equipamento-create'),
    path('equipamentos/<int:id>/update/', EquipamentoUpdateView.as_view(), name='equipamento-update'),
    path('equipamentos/<int:id>/delete/', EquipamentoDeleteView.as_view(), name='equipamento-delete'),
]
