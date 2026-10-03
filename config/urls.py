from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from acomodacoes.views import AcomodacaoViewSet

router = DefaultRouter()
router.register("acomodacoes", AcomodacaoViewSet, basename="acomodacao")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]