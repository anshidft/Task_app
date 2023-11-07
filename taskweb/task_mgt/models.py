from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=85, null=True)
    content = models.CharField(max_length=300, null=True)
    status = models.BooleanField(default=False, help_text='0=default, 1=Hidden',blank=True)
    date_posted = models.DateTimeField(auto_now=True, null=True)
    assignee = models.CharField(max_length=85, null=True, blank=True)

    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)


class Review(models.Model):
    reviwer_name = models.CharField(max_length=100)
    reviwe_title = models.CharField(max_length=85)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)