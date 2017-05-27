from __future__ import unicode_literals


from rest_framework import generics, permissions
from rest_framework.response import Response

from exercise.models import Exercise
from exercise.serializers import ExerciseSerializer
from day.permissionss import IsOwner


class ExerciseCreate(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Exercise.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ExerciseSerializer(queryset, many=True)
        return Response(serializer.data)


class ExerciseDetails(generics.RetrieveUpdateAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = (permissions, IsOwner)

    def get_queryset(self):
        user = self.request.user
        return Exercise.objects.filter(owner=user)
