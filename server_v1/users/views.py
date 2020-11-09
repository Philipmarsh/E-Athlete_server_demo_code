from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import User, FCMToken
from .serializers import UserSerializer, FCMTokenSerializer


class CurrentUser(APIView):

    def get(self, *args, **kwargs):
        serializer = UserSerializer(self.request.user)
        return Response(serializer.data)


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class FCMTokenView(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = FCMToken.objects.all()
    serializer_class = FCMTokenSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
