from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.core.exceptions import ValidationError
from django.contrib import messages
from app_colaborador.models import Colaborador
from app_equipamento.models import Equipamento
from .models import Emprestimo
from .forms import EmprestimoForm

# View funcional: formulário + listagem na mesma página
def emprestimo_view(request):
    if request.method == "POST":
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Empréstimo registrado com sucesso.")
                return redirect("emprestimo")
            except ValidationError as e:
                form.add_error(None, e)
                messages.error(request, e.message_dict.get('id_equipamento', ['Erro ao salvar'])[0])
                # Evita duplicidade de mensagens
                return render(request, "app_emprestimo/pages/emprestimo.html", {
                    "form": form,
                    "colaboradores": Colaborador.objects.all(),
                    "equipamentos": Equipamento.objects.all(),
                    "emprestimos": Emprestimo.objects.select_related("id_colaborador", "id_equipamento")
                })
        else:
            messages.error(request, "Erro ao registrar o empréstimo. Verifique os campos e tente novamente.")
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

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error(None, e)
            messages.error(self.request, e.message_dict.get('id_equipamento', ['Erro ao salvar'])[0])
            # Evita chamada duplicada de form_invalid
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao registrar o empréstimo. Verifique os campos e tente novamente.")
        return super().form_invalid(form)

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
