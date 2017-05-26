from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from authentication.serializers import UserSerializer


class UserCreate(APIView):
    """
    Create new user
    """
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]

    def post(self, request):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            User.objects.create_user(
                username=request.data['username'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                password=request.data['password']
            )
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

