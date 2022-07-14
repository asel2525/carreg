from rest_framework import routers

from cars.views import CarViewSet

router = routers.SimpleRouter()
router.register('cars', CarViewSet)

urlpatterns = []

urlpatterns += router.urls