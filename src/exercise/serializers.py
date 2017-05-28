from rest_framework import serializers

from exercise.models import Exercise, State


class ExerciseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validate_data):
        obj = Exercise.objects.create(**validate_data)
        obj.save()
        return obj

    class Meta:
        model = Exercise
        fields = ('id', 'name', 'owner')


class StateSerializer(serializers.ModelSerializer):

    def create(self, validate_data):
        obj = State.objects.create(**validate_data)
        obj.save()
        return obj

    class Meta:
        model = State
        fields = ('sensor_input_one', 'sensor_input_two')
