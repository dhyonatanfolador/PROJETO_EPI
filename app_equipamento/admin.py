from django.contrib import admin
from .models import Equipamento

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ("id", "descricao", "ca", "quantidade")
    search_fields = ("descricao", "ca")
    ordering = ("id",)
