from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from app_colaborador.models import Colaborador
from app_equipamento.models import Equipamento
from .models import Emprestimo
from .forms import EmprestimoForm


# View funcional: formulário + listagem na mesma página
def emprestimo_view(request):
    if request.method == "POST":
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("emprestimo")
    else:
        form = EmprestimoForm()

    context = {
        "form": form,
        "colaboradores": Colaborador.objects.all(),
        "equipamentos": Equipamento.objects.all(),
        "emprestimos": Emprestimo.objects.select_related("id_colaborador", "id_equipamento")
    }
    return render(request, "app_emprestimo/pages/emprestimo.html", context)


# Listagem separada
class EmprestimoListView(ListView):
    model = Emprestimo
    template_name = "app_emprestimo/pages/emprestimo.html"
    context_object_name = "emprestimos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["colaboradores"] = Colaborador.objects.all()
        context["equipamentos"] = Equipamento.objects.all()
        return context


# Criação separada
class EmprestimoCreateView(CreateView):
    model = Emprestimo
    form_class = EmprestimoForm
    template_name = "app_emprestimo/pages/emprestimo_form.html"
    success_url = reverse_lazy("emprestimo-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["colaboradores"] = Colaborador.objects.all()
        context["equipamentos"] = Equipamento.objects.all()
        return context


# Edição
class EmprestimoUpdateView(UpdateView):
    model = Emprestimo
    form_class = EmprestimoForm
    template_name = "app_emprestimo/pages/emprestimo_form.html"
    success_url = reverse_lazy("emprestimo-list")
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["colaboradores"] = Colaborador.objects.all()
        context["equipamentos"] = Equipamento.objects.all()
        return context


# Exclusão
class EmprestimoDeleteView(DeleteView):
    model = Emprestimo
    template_name = "app_emprestimo/pages/emprestimo_confirm_delete.html"
    success_url = reverse_lazy("emprestimo-list")
    pk_url_kwarg = "id"