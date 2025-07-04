# financas/views.py

from rest_framework import viewsets, permissions
from .models import Categoria, Gasto, Receita
from .serializers import CategoriaSerializer, GastoSerializer, ReceitaSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny # Para controle de acesso

# ViewSet para Categoria
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('nome') # Consulta base para todas as categorias
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated] # Somente usuários autenticados podem acessar

    def get_queryset(self):
        # Filtra categorias por usuário logado ou categorias globais (null=True)
        # Se for um superusuário, ele pode ver todas as categorias.
        if self.request.user.is_superuser:
            return Categoria.objects.all().order_by('nome')
        return Categoria.objects.filter(usuario=self.request.user) | Categoria.objects.filter(usuario__isnull=True).order_by('nome')

    def perform_create(self, serializer):
        # Ao criar uma categoria, associa ela automaticamente ao usuário logado,
        # a menos que o usuário seja um superusuário e não tenha fornecido um 'usuario'.
        if self.request.user.is_superuser and not serializer.validated_data.get('usuario'):
            serializer.save() # Permite criar categoria global pelo admin/superuser
        else:
            serializer.save(usuario=self.request.user)


# ViewSet para Gasto
class GastoViewSet(viewsets.ModelViewSet):
    queryset = Gasto.objects.all().order_by('-data_gasto')
    serializer_class = GastoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retorna apenas os gastos do usuário logado
        return Gasto.objects.filter(usuario=self.request.user).order_by('-data_gasto')

    def perform_create(self, serializer):
        # Ao criar um gasto, associa ele automaticamente ao usuário logado
        serializer.save(usuario=self.request.user)


# ViewSet para Receita
class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all().order_by('-data_receita')
    serializer_class = ReceitaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retorna apenas as receitas do usuário logado
        return Receita.objects.filter(usuario=self.request.user).order_by('-data_receita')

    def perform_create(self, serializer):
        # Ao criar uma receita, associa ela automaticamente ao usuário logado
        serializer.save(usuario=self.request.user)