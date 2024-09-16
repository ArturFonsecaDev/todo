from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class ToDo(models.Model):
    kanban_name = models.CharField(max_length=100)

    def __str__(self):
        return self.kanban_name

class Column(models.Model):
    name = models.CharField(max_length=45)
    position = models.IntegerField(null=False, blank=False)
    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE, related_name='columns')

    def __str__(self):
        return self.name

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.task_name}: {self.task_description}'
