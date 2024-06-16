from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    """Модель сотрудников для записи в БД"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    first_name = models.CharField(max_length=15, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=25, blank=True, verbose_name="Фамилия")
    date_of_birth = models.DateField()

    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"

    def __str__(self):
        return self.user.username


class Subscription(models.Model):
    """Модель подписки сотрудников"""

    subscriber = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subsciptios"
    )
    employee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscribers"
    )

    class Meta:
        verbose_name = "подписка"
        verbose_name_plural = "подписки"

    def __str__(self):
        return f"{self.subscriber.username} -> {self.employee.username}"
