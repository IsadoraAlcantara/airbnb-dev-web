from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=11)
    data_inicio_anfitriao = models.DateField(null=True, blank=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return f"{self.username} - {self.email} - {self.cpf} - {self.first_name} - {self.telefone}"