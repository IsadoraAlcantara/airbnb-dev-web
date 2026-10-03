from rest_framework.viewsets import ModelViewSet

from .models import Acomodacao
from .serializers import AcomodacaoSerializer


class AcomodacaoViewSet(ModelViewSet):
    queryset = Acomodacao.objects.all()
    serializer_class = AcomodacaoSerializer