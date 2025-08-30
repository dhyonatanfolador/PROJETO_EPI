from django.db import models

class Colaborador(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cargo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, null=True, blank=True)

def __str__(self):
    return self.nome
