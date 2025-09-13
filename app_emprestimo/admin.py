from django.contrib import admin
from .models import Emprestimo  # type: ignore

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ("id", "id_equipamento", "id_colaborador", "status")
    list_filter = ("status",)
    search_fields = ("id_equipamento__descricao", "id_colaborador__nome", "status")
    ordering = ("id",)
