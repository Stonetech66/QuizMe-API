from django.urls import path, include
from . import views
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView


API_TITLE=" STONE E-commerce API"
schema_view=get_swagger_view(title=API_TITLE)
urlpatterns=[ 
    path("<uuid:pk>/", views.MyQuestions.as_view(), name="user-questions"),
    path("", views.CreateQuestion.as_view(), name="create-question"),
    path("create-answers/", views.CreateAnswers.as_view(), name="create-answers"),
    path("answer-question/", views.AnswerQuestion.as_view(), name="answer-question"),
    path("docs/", schema_view, name="schema"),
    path("<int:pk>/", views.DeleteQuestionORUpdateQuestion.as_view(), name="update-question"),
    path('all/', views.ListallUsersAnswers.as_view(), name="all"),
    path("answers/<uuid:pk>/", views.AllAnswers.as_view(), name="all-users-answers"),
    path("my-answers/", views.MyAnswers.as_view()),
    path("", include('dj_rest_auth.urls')),
    path("signup/", include('dj_rest_auth.registration.urls')),
    path("password/reset/confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),


]