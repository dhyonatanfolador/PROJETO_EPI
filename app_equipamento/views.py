from rest_framework import generics
from .models import Equipamento
from .serializers import EquipamentoSerializer

class EquipamentoListView(generics.ListAPIView):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer

class EquipamentoCreateView(generics.CreateAPIView):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer

class EquipamentoUpdateView(generics.UpdateAPIView):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer
    lookup_field = 'id'

class EquipamentoDeleteView(generics.DestroyAPIView):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer
    lookup_field = 'id'
