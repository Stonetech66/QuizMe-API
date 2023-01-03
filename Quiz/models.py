from django.db import models
from Users.models import User
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError

# Create your models here.

class Question(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    question=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question}"



class Answers(models.Model):
    question=models.OneToOneField(Question, on_delete=models.CASCADE, related_name="question_answers")
    correct_answer=models.CharField(max_length=1000)
    wrong_answer_a=models.CharField(max_length=1000)
    wrong_answer_b=models.CharField(max_length=1000, null=True, blank=True)
    wrong_answer_c=models.CharField(max_length=1000, null=True, blank=True)
    wrong_answer_d=models.CharField(max_length=1000, null=True, blank=True)


    class Meta:
        verbose_name_plural= "Answers"
    
    def __str__(self):
        return self.correct_answer


class UserAnswer(models.Model):
    question=models.ForeignKey(Question, related_name="answers", on_delete=models.SET_NULL, null=True)
    answer=models.CharField(max_length=1000)
    date_added=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_answers")



    def __str__(self):
        return self.user.username

    