from django import forms
from .models import Emprestimo


class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = [
            "id_colaborador",
            "id_equipamento",
            "data_entrega",
            "data_devolucao",
            "devolucao",
            "status",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Impede edição da data de entrega sempre
        self.fields["data_entrega"].disabled = True

        # Ajusta o widget e formato da data_entrega
        self.fields["data_devolucao"].widget = forms.DateInput(attrs={"type": "date"})
        self.fields["data_devolucao"].input_formats = ["%Y-%m-%d"]

        self.fields["devolucao"].widget = forms.DateInput(attrs={"type": "date"})
        self.fields["devolucao"].input_formats = ["%Y-%m-%d"]

        data_entrega = forms.DateField(
            widget=forms.DateInput(attrs={"type": "date"}), input_formats=["%Y-%m-%d"]
        )

        if self.instance.pk:
            # Modo de edição: bloqueia colaborador e equipamento
            self.fields["id_colaborador"].disabled = True
            self.fields["id_equipamento"].disabled = True
        else:
            # Modo de criação: oculta certos status
            self.fields["status"].choices = [
                (value, label)
                for value, label in self.fields["status"].choices
                if value not in ["devolvido", "danificado", "perdido"]
            ]
