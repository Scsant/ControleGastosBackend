
# financas/admin.py

from django.contrib import admin
from .models import Categoria, Gasto, Receita # Importe os novos modelos

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'usuario')
    list_filter = ('tipo', 'usuario')
    search_fields = ('nome',)


@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data_gasto', 'categoria', 'usuario', 'forma_pagamento', 'criado_em')
    list_filter = ('categoria', 'usuario', 'forma_pagamento', 'data_gasto')
    search_fields = ('descricao', 'observacoes')
    date_hierarchy = 'data_gasto' # Permite navegar por data no admin


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data_receita', 'categoria', 'usuario', 'criado_em')
    list_filter = ('categoria', 'usuario', 'data_receita')
    search_fields = ('descricao', 'observacoes')
    date_hierarchy = 'data_receita' # Permite navegar por data no admin