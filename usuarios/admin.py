
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Registre seu modelo de usuário personalizado usando UserAdmin para uma interface rica
@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    pass # Use as configurações padrão do UserAdmin por enquanto