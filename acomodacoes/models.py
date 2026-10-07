from django.db import models


class Acomodacao(models.Model):
    titulo_acomodacao = models.CharField(max_length=100)
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    qtd_quartos = models.PositiveIntegerField(default=0)
    qtd_banheiros = models.PositiveIntegerField(default=0)
    qtd_camas = models.PositiveIntegerField(default=0)
    max_hospedes = models.PositiveIntegerField(default=1)
    status_hospedagem = models.BooleanField(default=True)
    # adicionar endereço

    def __str__(self):
        return f"{self.titulo_acomodacao} - R$ {self.valor_diaria} - {self.qtd_quartos} - {self.qtd_banheiros} - {self.qtd_camas} - {self.max_hospedes} - {self.status_hospedagem}"
