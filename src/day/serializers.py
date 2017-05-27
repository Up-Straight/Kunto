from rest_framework import serializers

from day.models import Day


class DaySerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Day
        fields = ('id', 'date', 'good_standing_time', 'bad_standing_time',
                  'total_time', 'done_training', 'owner')
