from rest_framework import routers
from .api import RiegoViewSet, AmbientesViewSet, MacetasViewSet, PlantasViewSet


router = routers.DefaultRouter()

router.register('api/riego', RiegoViewSet, 'riego')
router.register('api/ambientes', AmbientesViewSet, 'ambientes')
router.register('api/macetas', MacetasViewSet, 'macetas')
router.register('api/plantas', PlantasViewSet, 'plantas')

urlpatterns = router.urls