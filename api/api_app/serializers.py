from rest_framework import serializers
from pure_django_api.models import Poll, Choice
from django.contrib.auth.models import User


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields= ('id', 'created_by', 'question', 'pub_date')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'