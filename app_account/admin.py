from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "email", "telefone", "is_active")
    search_fields = ("nome", "email")
    list_filter = ("is_active",)
    ordering = ("id",)

