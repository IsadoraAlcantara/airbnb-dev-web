from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    search_fields = ("cpf",)
