from django.db import models
from app_equipamento.models import Equipamento  # type: ignore
from app_colaborador.models import Colaborador  # type: ignore

# Create your models here.
class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('emprestado', 'Emprestado'),
        ('em_uso', 'Em Uso'),
        ('fornecido', 'Fornecido'),
        ('devolvido', 'Devolvido'),
        ('danificado', 'Danificado'),
        ('perdido', 'Perdido'),
    ]

    id = models.AutoField(primary_key=True, editable=False, unique=True)
    id_colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    id_equipamento = models.ForeignKey(Equipamento, on_delete=models.PROTECT)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='fornecido')

    
    def __str__(self):
        return f"Empréstimo #{self.id} - {self.id_equipamento.descricao} para {self.id_colaborador.nome}"
    