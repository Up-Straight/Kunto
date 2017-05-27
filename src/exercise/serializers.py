from rest_framework import serializers

from exercise.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    states = serializers.SerializerMethodField('get_sensors')

    def get_sensors(self, obj):
        sol = []
        for state in obj.states:
            pair = [state.sensor_input_one, state.sensor_input_two]
            sol.append(pair)
        return sol

    def create(self, validate_data):
        obj = Exercise.objects.create(**validate_data)
        obj.save()
        return obj

    class Meta:
        model = Exercise
        fields = ('id', 'name', 'owner', 'states')
