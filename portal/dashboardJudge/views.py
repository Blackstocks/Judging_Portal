from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from customUser.decorators import judge_required
from django.conf import settings
from django.contrib import messages
from googleapiclient.discovery import build
from google.oauth2 import service_account
from django.shortcuts import get_object_or_404
from customUser.models import Participant, CustomUser, Judge
from scores.models import Score
import os
from django.dispatch import Signal
from scores.signals import score_created
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def create_score(judge, participant):
    score_created.send(sender=None, judge=judge, participant=participant)

@judge_required
@login_required
def dashboard(request):
    return render(request, 'dashboardJudge/dashboard.html')

@judge_required
@login_required
def judge(request, participant_username):
    if not participant_username == "choose_participant":
        user = get_object_or_404(CustomUser, username= participant_username)
        participant = get_object_or_404(Participant, user=user)
        embed_link = participant.ppt_link
    
        # Trigger the score creation
        judge = request.user.judge  # Assuming the logged-in user is a judge
        create_score(judge, participant)
        
        return render(request, 'dashboardJudge/judging.html', {'embed_link': embed_link})
    
    else:
        messages.success(request, 'Choose a participant')
        return redirect('judge_participants')

@judge_required
@login_required
def leaderboard(request):
    participants = Participant.objects.filter(rank__gt=0).order_by('rank')
    context = {'participants': participants}
    return render(request, 'dashboardJudge/leaderboard.html', context)

@judge_required
@login_required
def participants(request):
    users = CustomUser.objects.filter(is_participant=True).select_related('participant')
    return render(request, 'dashboardJudge/participants.html', {'users': users})

@judge_required
@login_required
@csrf_exempt
def create_score_view(request, participant_id, judge_id):
    if request.method == 'POST':
        score_data = request.POST.dict()

        # Extract the parameter values from the score_data dictionary
        p1 = float(score_data.get('p1', 0))
        p2 = float(score_data.get('p2', 0))
        p3 = float(score_data.get('p3', 0))
        p4 = float(score_data.get('p4', 0))
        p5 = float(score_data.get('p5', 0))
        p6 = float(score_data.get('p6', 0))
        p7 = float(score_data.get('p7', 0))
        p8 = float(score_data.get('p8', 0))
        p9 = float(score_data.get('p9', 0))
        p10 = float(score_data.get('p10', 0))

        # Calculate the total score
        total_score = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10

        # Get the participant and judge objects
        participant = Participant.objects.get(id=participant_id)
        judge = Judge.objects.get(id=judge_id)

        # Save the score to the database
        score = Score(total=total_score, parameters={
            'p1': p1,
            'p2': p2,
            'p3': p3,
            'p4': p4,
            'p5': p5,
            'p6': p6,
            'p7': p7,
            'p8': p8,
            'p9': p9,
            'p10': p10
        }, participant=participant, judge=judge)
        score.save()

        return JsonResponse({'message': 'Score created successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'})
