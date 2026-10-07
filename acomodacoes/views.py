from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .filters import AcomodacaoFilter
from .models import Acomodacao
from .serializers import AcomodacaoSerializer


class AcomodacaoViewSet(ModelViewSet):
    queryset = Acomodacao.objects.all()
    serializer_class = AcomodacaoSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AcomodacaoFilter