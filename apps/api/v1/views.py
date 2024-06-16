from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.employees.models import Employee, Subscription

from .serializers import (EmployeeSerializer, SubscriptionSerializer,
                          UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с моделью пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class EmployeeViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с моделью подписок"""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с моделью подписок"""

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
