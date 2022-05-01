from distutils import dep_util
from rest_framework import serializers
from .models import ExamAnswer, Profile, Question, Quiz

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class QuestionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class QuestionExamSerializer (serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'answer1', 'answer2', 'answer3', 'answer4']


class ExamAnswerSerializer (serializers.ModelSerializer):
    class Meta:
        model = ExamAnswer
        fields = '__all__'


class ExamResultSerializer (serializers.ModelSerializer):
    class Meta:
        model = ExamAnswer
        fields = '__all__'
        depth = 1


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 1


class ProfileSerializer (serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"


class Profile1Serializer (serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"
        depth = 1


class QuizSerializer (serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
