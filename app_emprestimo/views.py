from django.shortcuts import render
from rest_framework import generics
from .models import Emprestimo
from .serializers import EmprestimoSerializer

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import EmprestimoForm


class EmprestimoListView(generics.ListAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer


class EmprestimoUpdateView(generics.UpdateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    lookup_field = "id"


class EmprestimoDeleteView(generics.DestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    lookup_field = "id"


def Emprestimo(request):
    return render(request, "app_emprestimo/pages/emprestimo.html")


class EmprestimoCreateView(CreateView):
    model = Emprestimo
    form_class = EmprestimoForm
    template_name = "app_emprestimo/pages/emprestimo.html"
    success_url = reverse_lazy("emprestimo-list")

    def get_initial(self):
        return {"data_entrega"}
