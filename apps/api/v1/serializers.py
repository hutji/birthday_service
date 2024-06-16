from django.contrib.auth.models import User
from rest_framework import serializers

from apps.employees.models import Employee, Subscription


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя"""

    class Meta:
        model = User
        fields = ["id", "username", "email"]


class EmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор модели сотрудника"""

    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ["id", "user", "first_name", "last_name", "date_of_birth"]


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор подписок"""

    subscriber = UserSerializer()
    employee = UserSerializer()

    class Meta:
        model = Subscription
        fields = ["id", "subscriber", "employee"]
