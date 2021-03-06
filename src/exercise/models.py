from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    owner = models.ForeignKey(User, related_name='exercises', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50, blank=False,
                            default='')
    time = models.DurationField(null=True)

    def __unicode__(self):
        return self.name


class State(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='states', on_delete=models.CASCADE, null=True)
    sensor_input_one = models.IntegerField(default=0)
    sensor_input_two = models.IntegerField(default=0)

    def __unicode__(self):
        return self.exercise.name + " - " + \
               self.exercise.owner.username
