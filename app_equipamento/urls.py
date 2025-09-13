from django.urls import path
from .views import (
    EquipamentoListView,
    EquipamentoCreateView,
    EquipamentoUpdateView,
    EquipamentoDeleteView,
)

urlpatterns = [
    path('equipamentos/', EquipamentoListView.as_view(), name='equipamento-list'),
    path('equipamentos/create/', EquipamentoCreateView.as_view(), name='equipamento-create'),
    path('equipamentos/<int:id>/update/', EquipamentoUpdateView.as_view(), name='equipamento-update'),
    path('equipamentos/<int:id>/delete/', EquipamentoDeleteView.as_view(), name='equipamento-delete'),
]
