from django.db import models
from django.conf import settings


class Reserva(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reservas"
    )
    acomodacao = models.ForeignKey(
        "acomodacoes.Acomodacao", on_delete=models.CASCADE, related_name="reservas"
    )
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.usuario} - {self.acomodacao} - {self.data_inicio} - {self.data_fim} - {self.valor_total}"
