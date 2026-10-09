from rest_framework import serializers

from .models import Reserva


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = (
            "id",
            "usuario",
            "acomodacao",
            "data_inicio",
            "data_fim",
            "valor_total",
        )
