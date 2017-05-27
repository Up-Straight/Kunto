from rest_framework import serializers

from day.models import Day


class DaySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        obj = Day.objects.create(**validated_data)
        obj.save()
        return obj

    class Meta:
        model = Day
        fields = ('id', 'date', 'good_standing_time', 'bad_standing_time',
                  'total_time', 'done_training', 'owner')

