from django.shortcuts import render, redirect
import uuid
from django.utils import timezone
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Question, QuizSession, UserSubmission
from django.http import HttpResponse

@csrf_exempt
def start_quiz(request):
    """Start a new quiz session."""
    session_id = str(uuid.uuid4())
    QuizSession.objects.create(session_id=session_id)
    return render(request, 'api/quiz.html', {'session_id': session_id})

@csrf_exempt
def get_question(request, session_id):
    try:
        session = QuizSession.objects.get(session_id=session_id)
        if session.current_question:
            question = Question.objects.filter(id__gt=session.current_question.id).first()
        else:
            question = Question.objects.first()
            
        if not question:
            return HttpResponse("No more questions", status=404)

        session.current_question = question
        session.save()

        return render(request, 'api/questions.html', {
            'session_id': session_id,
            'question': question,
            'count' : session.correct_answers,
        })
    except QuizSession.DoesNotExist:
        return HttpResponse("Session not found", status=404)
    
@csrf_exempt
def submit_answer(request, session_id, question_id):
    try:
        session = QuizSession.objects.get(session_id=session_id)
        question = Question.objects.get(id=question_id)
        user_answer = request.POST.get('answer')
        is_correct = (user_answer == question.correct_answer)

        UserSubmission.objects.create(
            session=session,
            question=question,
            user_answer=user_answer,
            is_correct=is_correct
        )

        if is_correct:
            session.correct_answers += 1
        else:
            session.incorrect_answers +=1
        session.save()

        next_question = Question.objects.filter(id__gt=question.id).first()

        if next_question:
            return redirect(reverse('get_question', args=[session_id]))  
        else:
            return redirect(reverse('get_summary', args=[session_id]))

    except (QuizSession.DoesNotExist, Question.DoesNotExist):
        return HttpResponse("Invalid session or question", status=404)

@csrf_exempt
def get_summary(request, session_id):
    try:
        session = QuizSession.objects.get(session_id=session_id)
        
        if not session.end_time:
            session.end_time = timezone.now()
            session.save()
        
        end_time = session.end_time if session.end_time else timezone.now()
        time_spent = end_time - session.start_time
        seconds = time_spent.total_seconds()
        minutes = seconds // 60
        seconds = seconds % 60
        
        return render(request, 'api/summary.html',{
            "correct_answers": session.correct_answers,
            "incorrect_answers": session.incorrect_answers,
            "time_spent": f"{int(minutes)} minutes {int(seconds)} seconds"
        })

    except QuizSession.DoesNotExist:
        return JsonResponse({"error": "Session not found"}, status=404)
