
# financas/models.py

from django.db import models
from django.conf import settings # Para importar o seu modelo de usuário personalizado
# from .models import Categoria # Já importado se a Categoria estiver no mesmo arquivo

class Categoria(models.Model):
    # ... (Seu código existente para o modelo Categoria) ...
    TIPO_CHOICES = [
        ('despesa', 'Despesa'),
        ('receita', 'Receita'),
    ]

    nome = models.CharField(max_length=100, help_text="Nome da categoria (ex: Alimentação, Transporte)")
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='despesa',
                            help_text="Indica se é uma categoria de receita ou despesa.")
    
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='categorias',
        null=True, blank=True,
        help_text="Usuário proprietário da categoria. Deixe em branco para categorias globais."
    )

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        unique_together = ('nome', 'usuario') # Garante unicidade por usuário ou global
        ordering = ['tipo', 'nome']

    def __str__(self):
        if self.usuario:
            return f"{self.nome} ({self.get_tipo_display()}) - {self.usuario.username}"
        return f"{self.nome} ({self.get_tipo_display()}) - Global"


# --- Modelo Gasto ---
class Gasto(models.Model):
    # Campos que definimos no planejamento:
    descricao = models.CharField(max_length=255, help_text="Breve descrição do gasto (ex: Supermercado, Almoço)")
    valor = models.DecimalField(max_digits=10, decimal_places=2, help_text="Valor do gasto (ex: 150.75)")
    data_gasto = models.DateField(help_text="Data em que o gasto ocorreu.")
    
    # Relacionamento com Categoria (ForeignKey): Um gasto pertence a uma categoria
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL, # Se a categoria for deletada, não apaga o gasto, apenas seta para NULL
        related_name='gastos',    # Nome para o relacionamento reverso (categoria.gastos.all())
        null=True, blank=True,    # Permite gastos sem categoria, se a categoria for apagada
        limit_choices_to={'tipo': 'despesa'} # Sugestão: limita as categorias visíveis no Admin/Form para 'despesa'
    )
    
    # Relacionamento com Usuario (ForeignKey): Um gasto pertence a um usuário
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, # Se o usuário for deletado, apaga seus gastos
        related_name='gastos',    # Nome para o relacionamento reverso (user.gastos.all())
        help_text="Usuário que registrou este gasto."
    )
    
    # Campos adicionais (opcionais, mas úteis):
    FORMA_PAGAMENTO_CHOICES = [
        ('cartao_credito', 'Cartão de Crédito'),
        ('cartao_debito', 'Cartão de Débito'),
        ('dinheiro', 'Dinheiro'),
        ('pix', 'Pix'),
        ('boleto', 'Boleto'),
        ('transferencia', 'Transferência'),
        ('outros', 'Outros'),
    ]
    forma_pagamento = models.CharField(
        max_length=50,
        choices=FORMA_PAGAMENTO_CHOICES,
        blank=True, null=True,
        help_text="Forma de pagamento utilizada."
    )
    observacoes = models.TextField(
        blank=True, null=True,
        help_text="Notas adicionais sobre o gasto."
    )
    
    # Campos de timestamp (gerenciados automaticamente):
    criado_em = models.DateTimeField(auto_now_add=True) # Data e hora da criação do registro
    atualizado_em = models.DateTimeField(auto_now=True) # Data e hora da última atualização

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
        ordering = ['-data_gasto', '-criado_em'] # Ordenar por data mais recente, depois por criação

    def __str__(self):
        return f"Gasto de R${self.valor:.2f} em {self.data_gasto} ({self.categoria.nome if self.categoria else 'Sem Categoria'}) por {self.usuario.username}"


# --- Modelo Receita ---
class Receita(models.Model):
    # Campos que definimos no planejamento:
    descricao = models.CharField(max_length=255, help_text="Breve descrição da receita (ex: Salário, Freelance)")
    valor = models.DecimalField(max_digits=10, decimal_places=2, help_text="Valor da receita (ex: 1200.00)")
    data_receita = models.DateField(help_text="Data em que a receita foi recebida.")
    
    # Relacionamento com Categoria (ForeignKey): Uma receita pertence a uma categoria
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL, # Se a categoria for deletada, não apaga a receita, apenas seta para NULL
        related_name='receitas',   # Nome para o relacionamento reverso (categoria.receitas.all())
        null=True, blank=True,
        limit_choices_to={'tipo': 'receita'} # Sugestão: limita as categorias visíveis no Admin/Form para 'receita'
    )
    
    # Relacionamento com Usuario (ForeignKey): Uma receita pertence a um usuário
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, # Se o usuário for deletado, apaga suas receitas
        related_name='receitas',   # Nome para o relacionamento reverso (user.receitas.all())
        help_text="Usuário que registrou esta receita."
    )
    
    # Campos adicionais (opcionais):
    observacoes = models.TextField(
        blank=True, null=True,
        help_text="Notas adicionais sobre a receita."
    )
    
    # Campos de timestamp (gerenciados automaticamente):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        ordering = ['-data_receita', '-criado_em'] # Ordenar por data mais recente, depois por criação

    def __str__(self):
        return f"Receita de R${self.valor:.2f} em {self.data_receita} ({self.categoria.nome if self.categoria else 'Sem Categoria'}) por {self.usuario.username}"