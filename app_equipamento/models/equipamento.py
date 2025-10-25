from django.db import models

# Create your models here.
class Equipamento(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    ca = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    
    def __str__(self):
        return f"Empréstimo #{self.id}"

