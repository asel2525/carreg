from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from cars.serailizers import CarSerializer
from cars.models import Car

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [AllowAny, ]