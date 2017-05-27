from django.contrib.auth.models import User
from rest_framework import serializers

from day.models import Day


class UserSerializer(serializers.ModelSerializer):
    days = serializers.PrimaryKeyRelatedField(many=True, queryset=Day.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'days')
