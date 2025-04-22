from django.db import models
from django.conf import settings

class Task(models.Model):
    class Status(models.TextChoices):  # Enum defined inside the model
        TO_DO = 'TO DO', 'To Do'
        IN_PROGRESS = 'IN PROGRESS', 'In Progress'
        DONE = 'DONE', 'Done'

    name = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.TO_DO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_tasks'
    )

    def __str__(self):
        return self.name