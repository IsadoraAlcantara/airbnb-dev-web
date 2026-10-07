from rest_framework import serializers
from decimal import Decimal

from .models import Acomodacao


class AcomodacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acomodacao
        fields = (
            "id",
            "titulo_acomodacao",
            "valor_diaria",
            "qtd_quartos",
            "qtd_banheiros",
            "qtd_camas",
            "max_hospedes",
            "status_hospedagem",
        )

    def validate_titulo_acomodacao(self, value):
        titulo_limpo = value.strip()
        if len(titulo_limpo) < 3:
            raise serializers.ValidationError("O título da acomodação deve possui mais do que 3 caracteres")
        return titulo_limpo

    def validate_valor_diaria(self, value):
        if value <= Decimal("0"):
            raise serializers.ValidationError("O valor da diária deve ser maior do que zero")
        return value