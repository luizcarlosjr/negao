from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Cliente(models.Model):

    STATUS = (
        ('fazendo', 'Fazendo'),
        ('feito','Feito'),
    )

    Nome = models.CharField(max_length=200)
    Cpf = models.CharField(max_length=14, unique=True)
    Email = models.EmailField(unique=True)
    Indicacao = models.TextField()
    
    Status = models.CharField(
        max_length=7,
        choices=STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nome
