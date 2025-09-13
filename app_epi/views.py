from rest_framework import generics
from .models import Emprestimo
from .serializers import EmprestimoSerializer

class EmprestimoListView(generics.ListAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class EmprestimoCreateView(generics.CreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class EmprestimoUpdateView(generics.UpdateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    lookup_field = 'id'

class EmprestimoDeleteView(generics.DestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    lookup_field = 'id'
