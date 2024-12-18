from django.urls import path
from .views import start_quiz, get_question, submit_answer, get_summary

urlpatterns = [
    path("", start_quiz, name="start_quiz"),
    path("<str:session_id>/question/", get_question, name="get_question"),
    path("<str:session_id>/submit/<int:question_id>/", submit_answer, name="submit_answer"),
    path("<str:session_id>/summary/", get_summary, name="get_summary"),
]