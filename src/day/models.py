from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Day(models.Model):
    owner = models.ForeignKey(User, related_name='days', on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True, editable=False)
    coefficient = models.IntegerField(null=True)
    good_standing_time = models.DurationField(null=True)
    bad_standing_time = models.DurationField(null=True)
    total_time = models.DurationField(null=True)
    done_training = models.BooleanField(default=False)

    def __unicode__(self):
        return self.owner.username + " - " + str(self.date)