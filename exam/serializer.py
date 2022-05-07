from lib2to3.pgen2 import token
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import ExamAnswer, Profile, Question, Quiz, User
from django.contrib.auth.models import update_last_login


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):

        data = super().validate(attrs)
        print(data)
        token = self.get_token(self.user)
        
        data['email'] = self.user.email
        profile = Profile.objects.get(user=self.user)
        data['feild'] = profile.field
        data['full_name'] = profile.field
        data['state'] = profile.state
        data['id'] = profile.id
        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ("full_name", "field", "state", "note")


class UserRegistrationSerializer(serializers.ModelSerializer):

    profile = UserSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(
            user=user,
            full_name=profile_data['full_name'],
            state=profile_data['state'],
            note=profile_data['note'],
            field=profile_data['field']
        )
        return user


class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = user
            jwt_token = 'ss'
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email': user.email,
            'token': jwt_token,
            'id': user.id
        }


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


class User1Serializer (serializers.ModelSerializer):
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
