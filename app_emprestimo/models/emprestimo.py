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
        return (
            f"Empréstimo #{self.pk} – "
            f"{self.equipamento.descricao} para {self.colaborador.nome}"
        )

    def clean(self):
        super().clean()
        agora = timezone.now()

        # Garantir que a data prevista seja futura
        if self.data_prevista_devolucao <= agora:
            raise ValidationError({
                'data_prevista_devolucao': "Deve ser posterior à data e hora atuais."
            })

        # Se devolução já foi registrada, não pode ser antes da entrega
        if (
            self.data_efetiva_devolucao 
            and self.data_efetiva_devolucao < self.data_entrega
        ):
            raise ValidationError({
                'data_efetiva_devolucao': "Não pode ser anterior à data de entrega."
            })

    class Meta:
        ordering = ['-data_entrega']
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"

    