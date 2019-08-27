from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from . import serializers
from pure_django_api.models import Poll, Choice
from django.contrib.auth.models import User


class PollList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = serializers.PollSerializer
    queryset = Poll.objects.all()


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PollSerializer
    queryset = Poll.objects.all()
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAdminUser]


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ChoiceSerializer
    queryset = Choice.objects.all()
