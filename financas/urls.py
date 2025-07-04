# financas/urls.py

from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, GastoViewSet, ReceitaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'gastos', GastoViewSet)
router.register(r'receitas', ReceitaViewSet)

urlpatterns = router.urls