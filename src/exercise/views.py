from __future__ import unicode_literals


from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from exercise.models import Exercise
from exercise.serializers import ExerciseSerializer, StateSerializer
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


@api_view(['POST'])
def state_create(request):
    if request.method == 'POST':
        serializer = StateSerializer(data=request.data)
        id = request.data['exercise_id']
        if serializer.is_valid():
            exercise = Exercise.objects.get(id=id)
            serializer.save(exercise=exercise)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)