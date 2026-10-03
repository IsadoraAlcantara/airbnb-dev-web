from django.contrib import admin

from .models import Acomodacao


@admin.register(Acomodacao)
class AcomodacaoAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo_acomodacao", "valor_diaria", "qtd_quartos", "qtd_banheiros", "qtd_camas")
    search_fields = ("titulo_acomodacao",)
