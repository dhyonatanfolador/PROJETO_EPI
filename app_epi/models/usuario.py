from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True, null=False)
    nome = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    status = models.BooleanField(default=True)

def __str__(self):
    return f'Usuario(id={self.id}, nome="{self.nome}", email="{self.email}", status={self.status})'