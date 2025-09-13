from django import forms
from .models import Emprestimo

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ["id_colaborador", "id_equipamento", "data_entrega", "data_devolucao", "devolucao", "status"]