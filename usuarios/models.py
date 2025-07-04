from django.db import models

# usuarios/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # O AbstractUser já inclui campos como username, email, password,
    # first_name, last_name, is_staff, is_active, date_joined, etc.

    # Você pode adicionar campos extras aqui se precisar
    # Por exemplo, se quisesse um campo 'telefone':
    # telefone = models.CharField(max_length=20, blank=True, null=True)

    # Sobrescreva o campo email para ser único, se desejar (já é único no AbstractUser, mas bom reforçar)
    # email = models.EmailField(unique=True, blank=False, null=False) # Já configurado pelo AbstractUser

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['username'] # Ordenar por nome de usuário por padrão

    def __str__(self):
        return self.username # Ou self.email, dependendo de como você quer que apareça no admin
