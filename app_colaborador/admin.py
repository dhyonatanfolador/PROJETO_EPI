from django.contrib import admin
from .models import Colaborador  # type: ignore

# Register your models here.
@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):  # Corrigido nome da classe
    list_display = ("id", "nome", "email", "telefone", "cargo")
    search_fields = ("nome", "email", "cargo")
    ordering = ("id",)