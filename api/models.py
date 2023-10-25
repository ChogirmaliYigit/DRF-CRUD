from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Task(models.Model):
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'

    HIGH = 'high'
    MIDDLE = 'middle'
    LOW = 'low'

    STATUSES = (
        (TODO, 'ToDo'),
        (IN_PROGRESS, 'In progress'),
        (DONE, 'Done'),
    )

    PRIORITIES = (
        (HIGH, 'High'),
        (MIDDLE, 'Middle'),
        (LOW, 'Low'),
    )

    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUSES, default=TODO)
    priority = models.CharField(max_length=20, choices=PRIORITIES, default=MIDDLE)
    assignment = models.ForeignKey(User, models.CASCADE, 'user_tasks')
    category = models.ForeignKey(Category, models.CASCADE, 'category_tasks')

    def __str__(self):
        return self.title
