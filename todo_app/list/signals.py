from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from .models import TodoItem

@receiver(post_save, sender=TodoItem)
def create_repeated_todo_item(sender, instance, created, **kwargs):
    if not instance.completed:
        return
    
    if instance.repeat == 'none':
        return
    
    if not instance.due_date:
        return
    
    if instance.repeat == 'daily':
        next_due_date = instance.due_date + timedelta(days=1)

    elif instance.repeat == 'weekly':
        next_due_date = instance.due_date + timedelta(weeks=1)
    
    elif instance.repeat == 'monthly':
        next_due_date = instance.due_date + relativedelta(months=1)

    else:
        return
    
    TodoItem.objects.create(
        user=instance.user,
        category=instance.category,
        title=instance.title,
        description=instance.description,
        due_date=next_due_date,
        due_time=instance.due_time,
        reminder_minutes=instance.reminder_minutes,
        repeat=instance.repeat,
    )