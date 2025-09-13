from django import forms
from .models import Colaborador

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            # outros campos aqui
        }
        labels = {
            'nome': 'Nome Completo',
            'cargo': 'Cargo',
            'email': 'Email',
            'telefone': 'Telefone',
            # outros campos aqui
        }
        help_texts = {
            'email': 'Insira um email válido.',
            'telefone': 'Formato: (XX) XXXXX-XXXX',
            # outros campos aqui
        }
        error_messages = {
            'nome': {
                'max_length': 'O nome é muito longo.',
                'required': 'O nome é obrigatório.',
            },
            'email': {
                'invalid': 'Insira um email válido.',
                'required': 'O email é obrigatório.',
            },
            # outros campos aqui
        }