from django.urls import path
from .views import DiaristasCidadeLista

urlpatterns = [
    path('diaristas-cidade', DiaristasCidadeLista.as_view(), name='ciaristas-cidade-lista'),
]
