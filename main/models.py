from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    complete = models.BooleanField(default=False, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)

