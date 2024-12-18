from django.db import models
from django.utils import timezone
import uuid


class Question(models.Model):
    U_id = models.CharField(max_length=10, default="", unique=False)
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1)  
    is_default = models.BooleanField(default=False) 

    def __str__(self):
        return self.question_text

class QuizSession(models.Model):
    session_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    current_question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.SET_NULL) 
    correct_answers = models.PositiveIntegerField(default=0)
    incorrect_answers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Session {self.session_id}"
    
class UserSubmission(models.Model):
    session = models.ForeignKey(QuizSession, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=1) 
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Session: {self.session.id}, Question: {self.question.id}"
