from __future__ import unicode_literals

from rest_framework import generics, permissions

from day.models import Day
from day.serializers import DaySerializer
from permissionss import IsOwner


class DayCreate(generics.ListCreateAPIView):
    serializer_class = DaySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Day.objects.filter(owner=user)


class DayDetails(generics.RetrieveUpdateAPIView):
    serializer_class = DaySerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        user = self.request.user
        return Day.objects.filter(owner=user)

