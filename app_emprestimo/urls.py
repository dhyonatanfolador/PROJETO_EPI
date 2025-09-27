from django.urls import path
from .views import (
    emprestimo_view,
    EmprestimoListView,
    EmprestimoCreateView,
    EmprestimoUpdateView,
)

urlpatterns = [
    # Página principal com formulário + listagem
    path('emprestimo/', emprestimo_view, name='emprestimo'),

    # CRUD separado (opcional)
    path('emprestimos', EmprestimoListView.as_view(), name='emprestimo-list'),
    path('emprestimos/create/', EmprestimoCreateView.as_view(), name='emprestimo-create'),
    path('emprestimos/<int:id>/update/', EmprestimoUpdateView.as_view(), name='emprestimo-update'),
]