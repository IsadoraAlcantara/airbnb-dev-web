from django.db import models

class Acomodacao(models.Model):
    titulo_acomodacao = models.CharField(max_length=100)
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    qtd_quartos = models.PositiveIntegerField(default=0)
    qtd_banheiros = models.PositiveIntegerField(default=0)
    qtd_camas = models.PositiveIntegerField(default=0)
    # adicionar endereço

    def __str__(self):
        return f"{self.titulo_acomodacao} - R$ {self.valor_diaria} - {self.qtd_quartos} - {self.qtd_banheiros} - {self.qtd_camas}"

