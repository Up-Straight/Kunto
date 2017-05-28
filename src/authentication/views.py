from __future__ import unicode_literals
from django.contrib.auth.models import User

from rest_framework import status, permissions
from rest_framework import views, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from authentication.serializers import UserSerializer


class UserCreate(views.APIView):
    permission_classes = [
        permissions.AllowAny
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


class UserGet(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permissions_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.pk)


@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


