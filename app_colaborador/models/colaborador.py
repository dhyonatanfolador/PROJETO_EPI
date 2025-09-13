from django.db import models

# Create your models here.
class Colaborador(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cargo = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
