from rest_framework import serializers
from .models import ExamAnswer, Profile, Question, Quiz

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class QuestionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class ExamAnswerSerializer (serializers.ModelSerializer):
    class Meta:
        model = ExamAnswer
        fields = '__all__'


class ProfileSerializer (serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"


class QuizSerializer (serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
