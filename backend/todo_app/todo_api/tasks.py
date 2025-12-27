from django.core.mail import send_mail
from celery import shared_task
from django.utils import timezone
from list.models import TodoItem
from datetime import datetime, timedelta

@shared_task

# Task to send reminders for upcoming todo items
def send_todo_reminders():
    # Get current time 
    now = timezone.now()
    # Query for todo items that are not completed and have a due date, due time, and reminder set
    todo_items = TodoItem.objects.filter(
        completed=False,
        due_date_isnull=False,
        due_time_isnull=False,
        reminder_minutes_isnull=False
    )
    # Iterate through todo items and check if a reminder should be sent

    for todo in todo_items:
        due_datetime = timezone.make_aware(
            datetime.combine(todo.due_date, todo.due_time)
        )
        # Calculate the reminder time

        reminder_time = due_datetime - timedelta(minutes=todo.reminder_minutes)
        
        # Check if it's time to send a reminder

        if now >= reminder_time and now < due_datetime:
            #if you want to send on email reminder uncomment the line below
            # send_reminder_email(todo)
            print(f"Reminder: Task '{todo.title}' is due at {due_datetime}.")


@shared_task

def test_task():
    print("Celery is working!")