from django.contrib import admin
from .models import  Question, Answers, UserAnswer
# Register your models here.

class AnswerInline(admin.StackedInline):
    model=Answers

class QuestionAdmin(admin.ModelAdmin):
    list_display=["user", ]
    search_fields= ["user__username", "user__email", "body"]
    inlines=[AnswerInline]


admin.site.register(Question,QuestionAdmin)
admin.site.register(Answers)
admin.site.register(UserAnswer)