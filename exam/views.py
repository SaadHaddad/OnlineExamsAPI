from asyncio.windows_events import NULL
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from .models import Quiz, Question, ExamAnswer, Profile, User
from .serializer import ExamAnswerSerializer, ExamResultSerializer, MyTokenObtainPairSerializer, Profile1Serializer, ProfileSerializer, QuestionExamSerializer, QuestionSerializer, QuizSerializer, UserLoginSerializer, UserRegistrationSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from django.http import Http404
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
# create user


class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'User registered  successfully',
        }

        return Response(response, status=status_code)


class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token': serializer.data['token'],
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)


class Fun(APIView):
    def post(self, request, user_id):

        answers = request.data.get('data')
        is_many = isinstance(answers, list)
        print(request.data)
        if not is_many:
            serializer = ExamAnswerSerializer(data=answers)
            if serializer.is_valid():
                serializer.save()
                # update user state
                Profile.objects.filter(pk=user_id).update(state=True)
                return Response(answers, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ExamAnswerSerializer(data=answers, many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                Profile.objects.filter(pk=user_id).update(state=True)
                return Response(answers, status=status.HTTP_201_CREATED)


class User_List(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        guests = User.objects.all()
        serializer = UserSerializer(guests, many=True)
        return Response(serializer.data)


class User_result_pk(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return ExamAnswer.objects.filter(user=pk)
        except ExamAnswer.DoesNotExists:
            raise Http404

    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = ExamResultSerializer(guest, many=True)
        return Response(serializer.data)


class Quiz_List(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        guests = Quiz.objects.all()
        serializer = QuizSerializer(guests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# ------------------------- quiz--------------------------------
class Quiz_pk(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Quiz.objects.get(pk=pk)
        except Quiz.DoesNotExists:
            raise Http404

    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = QuizSerializer(guest)
        return Response(serializer.data)

    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = QuizSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------- anserr--------------------------------


class Answer_List(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        guests = ExamAnswer.objects.all()
        serializer = ExamAnswerSerializer(guests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExamAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class Answer_pk(APIView):

    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return ExamAnswer.objects.get(pk=pk)
        except ExamAnswer.DoesNotExists:
            raise Http404

    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = ExamAnswerSerializer(guest)
        return Response(serializer.data)

    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = ExamAnswerSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------------- Question--------------------------------

class QuestionExam_List(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk):
        prof = Profile.objects.get(pk=pk)
        if prof.state:
            return Response("No Question")
        else:
            guests = Question.objects.all()
            serializer = QuestionExamSerializer(guests, many=True)
            return Response(serializer.data)


class Question_List(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        guests = Question.objects.all()
        serializer = QuestionSerializer(guests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class Question_pk(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExists:
            raise Http404

    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = QuestionSerializer(guest)
        return Response(serializer.data)

    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = QuestionSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ------------------------- profile --------------------------------


class Profile_List(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        guests = Profile.objects.all()
        serializer = Profile1Serializer(guests, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class Profile_pk(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExists:
            raise Http404

    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = ProfileSerializer(guest)
        return Response(serializer.data)

    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = ProfileSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
