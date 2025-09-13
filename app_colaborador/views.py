from django.shortcuts import render
from .models import Colaborador
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ColaboradorForm
from django.contrib import messages


# Listar todos os colaboradores
class ColaboradorListView(ListView):
    model = Colaborador
    template_name = 'app_colaborador/pages/colaborador.html'
    context_object_name = 'colaboradores'
    paginate_by = 10

class ColaboradorCreateView(CreateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'app_colaborador/pages/colaborador_form.html'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Colaborador criado com sucesso!")
        return self.render_to_response(self.get_context_data(form=self.form_class()))

class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = 'app_colaborador/pages/colaborador_form.html'
    success_url = reverse_lazy('colaborador-list')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, "Colaborador atualizado com sucesso!")
        return super().form_valid(form)

class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    template_name = 'app_colaborador/pages/colaborador_confirm_delete.html'
    success_url = reverse_lazy('colaborador-list')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, "Colaborador deletado com sucesso!")
        return super().form_valid(form)
