from django.contrib import admin

from .models import Reserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("id", "data_inicio", "data_fim", "valor_total")
    # search_fields = ("nome",)