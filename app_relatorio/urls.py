from django.urls import path
from .views import relatorio_emprestimos_view, GerarPdfView

urlpatterns = [
    path('relatorio/', relatorio_emprestimos_view, name='relatorio-emprestimos'),
    path('relatorio/pdf/', GerarPdfView.as_view(), name='relatorio-pdf'),
]
