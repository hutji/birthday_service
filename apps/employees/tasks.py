from datetime import date

from celery import shared_task
from django.core.mail import send_mail

from .models import Employee, Subscription


@shared_task
def send_birthday_notification():
    today = date.today()
    employees = Employee.objects.filter(
        date_of_birth__month=today.month, date_of_birth__day=today.day
    )
    for employee in employees:
        subscribers = Subscription.objects.filter(employee=employee).value_list(
            "subscriber__email", flat=True
        )
        if subscribers:
            send_mail(
                "С Днем Рождения",
                f"Сегодня День Рождения {employee.user.username}",
                subscribers,
            )
