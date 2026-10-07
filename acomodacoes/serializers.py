from rest_framework import serializers

from .models import Acomodacao


class AcomodacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acomodacao
        fields = ("id", "titulo_acomodacao", "valor_diaria", "qtd_quartos", "qtd_banheiros", "qtd_camas", "max_hospedes", "status_hospedagem")