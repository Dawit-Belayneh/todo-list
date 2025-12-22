from celery import shared_task
from django.utils import timezone
from list.models import TodoItem
from datetime import timedelta

@shared_task

def send_todo_reminders():
    now = timezone.now()
    todo_items = TodoItem.objects.filter(
        completed=False,
        due_date_isnull=False,
        due_time_isnull=False,
        reminder_minutes_isnull=False
    )

    for item in todo_items:
        due_datetime = timezone.make_aware(
            
        )


