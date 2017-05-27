from __future__ import unicode_literals


from rest_framework import generics, permissions
from rest_framework.response import Response

from day.models import Day
from day.serializers import DaySerializer
from permissionss import IsOwner


class DayCreate(generics.ListCreateAPIView):
    serializer_class = DaySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Day.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = DaySerializer(queryset, many=True)
        return Response(serializer.data)


class DayDetails(generics.RetrieveUpdateAPIView):
    serializer_class = DaySerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        user = self.request.user
        return Day.objects.filter(owner=user)

