from rest_framework import serializers
from .models import Question, Answers, UserAnswer
from Users.models import User

class Answers_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Answers
        fields=[
        "question", 
        "correct_answer" ,
        "wrong_answer_a",
        "wrong_answer_b",
        "wrong_answer_c",
        "wrong_answer_d"
]

    def validate_question(self, value):
        q=Question.objects.filter(id=value.id)
        request=self.context.get("request")
        if not q[0].user == request.user:
            raise serializers.ValidationError("You can't create answers for this question it belongs to another user")
        return value


class Question_Serializer(serializers.ModelSerializer):
    answers=Answers_Serializer(source="question_answers",read_only=True)
    id=serializers.CharField(read_only=True)
    user=serializers.StringRelatedField()
    class Meta:
        model=Question
        fields=[ 
            "id",
            "question",
            'answers',
            'user'
        ]


class UserQuestions_Serializer(serializers.ModelSerializer):
    questions=Question_Serializer(many=True, read_only=True)
    class Meta:
        model=User
        fields=[
            "id",
            "username",
            "questions"
        ]

class AnswerQuestionSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        model=UserAnswer
        fields=[ 
            "id",
            "user",
            "answer",
            "question",
            "date_added"
        ]

class AllUsersAnswersSerializer(serializers.ModelSerializer):
    Question=Question_Serializer(read_only=True, source="question")
    class Meta:
        model=UserAnswer
        fields=[ 
            "question",
            "Question",
            "answer",
            "date_added",
   ]

class UserAnswers(serializers.ModelSerializer):
    questions=serializers.SerializerMethodField()
    class Meta:
        model=User
        fields=[
            "username",
            "questions"
        ]

    def get_questions(self, obj):
        request=self.context.get('request')
        return AllUsersAnswersSerializer(obj.user_answers.all().filter(question__user=request.user), many=True).data


class ListUsersAnswers(serializers.ModelSerializer):
    username=serializers.StringRelatedField(source="user")
    url=serializers.URLField(source="user.get_answers_url")
    class Meta:
        model=UserAnswer
        fields=[ 
            "user",
            "url",
            "username"
        ]

