from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Quiz, Question, ExamAnswer, Profile
from .serializer import ExamAnswerSerializer, ProfileSerializer, QuestionSerializer, QuizSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from django.http import Http404


def fun(request):
    return JsonResponse({'sssss': 'sss'})


class Quiz_List(APIView):
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
            serializer.data,
            status=status.HTTP_400_BAD_REQUEST
        )


# 4.2 GET PUT DELETE cloass based views - - pk


class Quiz_pk(APIView):

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
            serializer.data,
            status=status.HTTP_400_BAD_REQUEST
        )


class Answer_pk(APIView):

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

class Question_List(APIView):
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
            serializer.data,
            status=status.HTTP_400_BAD_REQUEST
        )


class Question_pk(APIView):

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
    def get(self, request):
        guests = Profile.objects.all()
        serializer = ProfileSerializer(guests, many=True)
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
            serializer.data,
            status=status.HTTP_400_BAD_REQUEST
        )


class Profile_pk(APIView):

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
