# financas/serializers.py

from rest_framework import serializers
from .models import Categoria, Gasto, Receita
from django.contrib.auth import get_user_model # Para obter o modelo de usuário personalizado

User = get_user_model() # Obtém o seu modelo de usuário 'Usuario'

# Serializer para o modelo de Usuário (apenas o necessário para exibir)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name') # Campos que você quer expor

# Serializer para o modelo Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    # Opcional: Se quiser que o nome do usuário apareça em vez do ID
    # usuario = UserSerializer(read_only=True) # Se quiser exibir detalhes do usuário

    class Meta:
        model = Categoria
        fields = '__all__' # Inclui todos os campos do modelo Categoria

# Serializer para o modelo Gasto
class GastoSerializer(serializers.ModelSerializer):
    # Exibe o nome da categoria e o nome do usuário em vez de apenas os IDs
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)
    usuario_username = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = Gasto
        fields = '__all__' # Inclui todos os campos do modelo Gasto
        read_only_fields = ['usuario']  # 👈 ESSENCIAL!
        # Ou especifique os campos que você quer, incluindo os novos que criamos:
        # fields = ('id', 'descricao', 'valor', 'data_gasto', 'categoria', 'categoria_nome', 'usuario', 'usuario_username', 'forma_pagamento', 'observacoes', 'criado_em', 'atualizado_em')

# Serializer para o modelo Receita
class ReceitaSerializer(serializers.ModelSerializer):
    # Exibe o nome da categoria e o nome do usuário em vez de apenas os IDs
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)
    usuario_username = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = Receita
        fields = '__all__' # Inclui todos os campos do modelo Receita
        # fields = ('id', 'descricao', 'valor', 'data_receita', 'categoria', 'categoria_nome', 'usuario', 'usuario_username', 'observacoes', 'criado_em', 'atualizado_em')