from django.urls import path
from .views import (
    EmprestimoListView,
    EmprestimoCreateView,
    EmprestimoUpdateView,
    EmprestimoDeleteView,
)

urlpatterns = [
    path('emprestimos/', EmprestimoListView.as_view(), name='emprestimo-list'),
    path('emprestimos/create/', EmprestimoCreateView.as_view(), name='emprestimo-create'),
    path('emprestimos/<int:id>/update/', EmprestimoUpdateView.as_view(), name='emprestimo-update'),
    path('emprestimos/<int:id>/delete/', EmprestimoDeleteView.as_view(), name='emprestimo-delete'),
]
