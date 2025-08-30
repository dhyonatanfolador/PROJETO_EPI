from django.db import models

class Equipamento(models.Model):
    ca = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    quantidade = models.PositiveIntegerField()

def __str__(self):
    return f"{self.nome} (CA: {self.ca})"
