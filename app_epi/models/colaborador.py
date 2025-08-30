from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cargo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, null=True, blank=True)

def __str__(self):
    return self.nome
