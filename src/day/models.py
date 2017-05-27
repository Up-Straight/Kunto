from __future__ import unicode_literals

from django.db import models


class Day(models.Model):
    date = models.DateField(auto_now_add=True, editable=False)
    coefficient = models.IntegerField(null=True)
    good_standing_time = models.DurationField()
    bad_standing_time = models.DurationField()
    total_time = models.DurationField()
    done_training = models.BooleanField(default=False)