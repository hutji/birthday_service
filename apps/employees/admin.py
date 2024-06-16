from django.contrib import admin

from .models import Employee, Subscription


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Админка сотрудников"""

    list_display = ("id", "user", "first_name", "last_name", "date_of_birth")
    search_fields = ("user", "date_of_birth")


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """Админка подписок"""

    list_display = (
        "id",
        "subscriber",
        "employee",
    )
    search_fields = ("subscriber", "employee")
