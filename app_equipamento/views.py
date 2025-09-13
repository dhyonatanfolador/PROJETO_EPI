from django.shortcuts import render
from .models import Equipamento
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import EquipamentoForm
from django.contrib import messages

class EquipamentoListView(ListView):
    model = Equipamento
    template_name = 'app_equipamento/pages/equipamento.html'
    context_object_name = 'equipamentos'
    paginate_by = 10

class EquipamentoCreateView(CreateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = 'app_equipamento/pages/equipamento_form.html'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Equipamento criado com sucesso!")
        return self.render_to_response(self.get_context_data(form=self.form_class()))

class EquipamentoUpdateView(UpdateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = 'app_equipamento/pages/equipamento_form.html'
    success_url = reverse_lazy('equipamento-list')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, "Equipamento atualizado com sucesso!")
        return super().form_valid(form)

class EquipamentoDeleteView(DeleteView):
    model = Equipamento
    template_name = 'app_equipamento/pages/equipamento_confirm_delete.html'
    success_url = reverse_lazy('equipamento-list')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, "Equipamento deletado com sucesso!")
        return super().form_valid(form)

