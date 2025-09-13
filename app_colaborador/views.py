from django.shortcuts import render
from rest_framework import generics
from .models import Colaborador
from .serializers import ColaboradorSerializer

# Listar todos os colaboradores
class ColaboradorListView(generics.ListAPIView):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer

# Criar um novo colaborador
class ColaboradorCreateView(generics.CreateAPIView):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer

# Atualizar um colaborador pelo ID
class ColaboradorUpdateView(generics.UpdateAPIView):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer
    lookup_field = 'id'  # campo usado na URL para identificar o colaborador

# Deletar um colaborador pelo ID
class ColaboradorDeleteView(generics.DestroyAPIView):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer
    lookup_field = 'id'

def Colaborador(request):
    return render(request, "app_colaborador/pages/colaborador.html") 
