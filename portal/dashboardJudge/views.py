from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from customUser.decorators import judge_required
from django.conf import settings
from django.shortcuts import render
from googleapiclient.discovery import build
from google.oauth2 import service_account
from django.shortcuts import get_object_or_404
from customUser.models import Participant, CustomUser
import os

@judge_required
@login_required
def dashboard(request):
    return render(request, 'dashboardJudge/dashboard.html')

@judge_required
@login_required
def judge(request, participant_username):
    user = get_object_or_404(CustomUser, username= participant_username)
    participant = get_object_or_404(Participant, user=user)
    embed_link = participant.ppt_link
    return render(request, 'dashboardJudge/judging.html', {'embed_link': embed_link})

@judge_required
@login_required
def leaderboard(request):
    return render(request, 'dashboardJudge/leaderboard.html')

