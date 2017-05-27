from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    owner = models.ForeignKey(User, related_name='states', on_delete=models.CASCADE, default=1)
    time = models.DurationField()


class State(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='states', on_delete=models.CASCADE, default=1)
    sensor_input_one = models.IntegerField(default=0)
    sensor_input_two = models.IntegerField(default=0)