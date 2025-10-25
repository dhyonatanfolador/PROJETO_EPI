from django.shortcuts import render, redirect
from .models import Equipamento
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import EquipamentoForm
from django.contrib import messages
from django.db.models import ProtectedError

class EquipamentoListView(ListView):
    model = Equipamento
    template_name = "app_equipamento/pages/equipamento.html"
    context_object_name = "equipamentos"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q", "").strip()
        if q:
            queryset = queryset.filter(nome__icontains=q)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # para manter o termo pesquisado no input do template
        context["q"] = self.request.GET.get("q", "")
        return context


class EquipamentoCreateView(CreateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = "app_equipamento/pages/equipamento_form.html"

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Equipamento criado com sucesso!")
        return self.render_to_response(self.get_context_data(form=self.form_class()))


class EquipamentoUpdateView(UpdateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = "app_equipamento/pages/equipamento_form.html"
    success_url = reverse_lazy("equipamento-list")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        messages.success(self.request, "Equipamento atualizado com sucesso!")
        return super().form_valid(form)


class EquipamentoDeleteView(DeleteView):
    model = Equipamento
    template_name = 'app_equipamento/pages/equipamento_confirm_delete.html'
    success_url = reverse_lazy('equipamento-list')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, "Equipamento deletado com sucesso!")
            return response
        except ProtectedError:
            messages.error(self.request, "Não é possível deletar este equipamento pois ele está vinculado a empréstimos ativos.")
            return redirect(self.success_url)