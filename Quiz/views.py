from .models import Answers, Question, UserAnswer
from Users.models import User
from .serializers import  AllUsersAnswersSerializer, AnswerQuestionSerializer, Answers_Serializer, ListUsersAnswers, Question_Serializer, UserAnswers, UserQuestions_Serializer
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsOwner
from django.shortcuts import get_object_or_404

# Create your views here.


class MyQuestions(generics.RetrieveAPIView):
    """
    Returns a list of all the user questions
    """
    serializer_class=UserQuestions_Serializer
    queryset=User.objects.all()
    permission_classes= []



class CreateQuestion(generics.CreateAPIView):
    """
    For creating a Question 
    """
    serializer_class=Question_Serializer
    queryset=Question.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CreateAnswers(generics.CreateAPIView):
    """
    To be used with the Creating question url.
    For creating answers for a particular question.
    The id of the question is to be inputed
    """
    serializer_class=Answers_Serializer
    queryset=Answers.objects.all()


class AnswerQuestion(generics.CreateAPIView):
    """
    For a user to a answer a particular question.
    Note: The answer field should be a select field from the Create Answers url and the user input should be used in the answer field
    """
    queryset=UserAnswer.objects.all()
    serializer_class=AnswerQuestionSerializer 

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class DeleteQuestionORUpdateQuestion(generics.RetrieveUpdateDestroyAPIView):
    """
    To delete and update a particular question
    """
    serializer_class= Question_Serializer
    queryset=Question.objects.all()
    permission_classes=[permissions.IsAuthenticated ,IsOwner]

class AllAnswers(generics.RetrieveAPIView):
    """
    To Get a particular user and list all the question he has answered
    """
    serializer_class=UserAnswers
    queryset=User.objects.all()

class MyAnswers(generics.ListAPIView):
    """
    A list of all the questions a user has answered
    """
    serializer_class=AllUsersAnswersSerializer

    def get_queryset(self):
        return UserAnswer.objects.filter(user=self.request.user).select_related("user", "question").prefetch_related("question__question_answers")

class ListallUsersAnswers(generics.ListAPIView):
    """
    A list of all the users that have answered a user question
    """
    serializer_class=ListUsersAnswers

    def get_queryset(self):
        return UserAnswer.objects.filter(question__user=self.request.user).select_related("question", "user")







