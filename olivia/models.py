from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group, related_name='olivia_users', blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='olivia_users', blank=True)


class Routine(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class RoutineSteps(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    start_time = models.TimeField()
    end_time = models.TimeField()
    complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.description
