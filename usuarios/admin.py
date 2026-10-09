from django.contrib import admin

from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "cpf", "first_name", "telefone", "data_nascimento", "data_inicio_anfitriao")
    search_fields = ("username", "email", "cpf",)