from django.contrib import admin
from .models import Usuario


# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "email", "telefone", "status")
    search_fields = ("nome", "email")
    list_filter = ("status",)
    ordering = ("id",)
