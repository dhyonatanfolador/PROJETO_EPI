from django.db import models
from django.conf import settings
from .colaborador import Colaborador
from .equipamento import Equipamento

class Emprestimo(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    data_retirada = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=True)

def __str__(self):
    return f"Empréstimo #{self.id} - {self.equipamento.nome} para {self.colaborador.nome}"
