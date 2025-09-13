from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from app_equipamento.models import Equipamento  # type: ignore
from app_colaborador.models import Colaborador  # type: ignore

class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('emprestado', 'Emprestado'),
        ('em_uso',    'Em Uso'),
        ('fornecido', 'Fornecido'),
        ('devolvido', 'Devolvido'),
        ('danificado','Danificado'),
        ('perdido',   'Perdido'),
    ]

    id_colaborador = models.ForeignKey(
        Colaborador,
        on_delete=models.PROTECT,
        verbose_name="Colaborador"
    )
    id_equipamento = models.ForeignKey(
        Equipamento,
        on_delete=models.PROTECT,
        verbose_name="Equipamento"
    )
    data_entrega = models.DateTimeField(
        default=timezone.now,
        verbose_name="Data de Entrega"
    )
    data_devolucao = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Data revista de Devolução"
    )

    devolucao = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Data Efetiva de Devolução"
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='fornecido',
        verbose_name="Status"
    )

def __str__(self):
    return f"Empréstimo #{self.pk} – {self.id_equipamento.descricao} para {self.id_colaborador.nome}"

def clean(self):
    super().clean()
    agora = timezone.now()

    if self.data_devolucao and self.data_devolucao <= agora:
        raise ValidationError({
            'data_devolucao': "Deve ser posterior à data e hora atuais."
        })

    if self.devolucao and self.devolucao < self.data_entrega:
        raise ValidationError({
            'devolucao': "Não pode ser anterior à data de entrega."
        })

    class Meta:
        ordering = ['-data_entrega']
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"

    