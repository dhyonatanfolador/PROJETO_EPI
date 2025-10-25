from django.contrib import admin
from .models import Equipamento

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "ca", "quantidade")
    search_fields = ("nome", "ca")
    ordering = ("id",)
