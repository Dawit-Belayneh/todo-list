from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass

class TodoItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title =  models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    due_time = models.TimeField(null=True, blank=True)
    reminder_minutes = models.PositiveIntegerField(null=True, blank=True, help_text="Minutes before due time to remind")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)