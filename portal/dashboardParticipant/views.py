from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from customUser.decorators import participant_required
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404
from customUser.models import Participant, CustomUser, Judge
from scores.models import Score
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.views import LoginView

@login_required
@participant_required
def dashboard(request):
    return render(request, 'dashboardParticipant/dashboard.html')

@login_required
@participant_required
def leaderboard(request):
    participants = Participant.objects.filter(rank__gt=0).order_by('rank')
    context = {'participants': participants}
    return render(request, 'dashboardParticipant/leaderboard.html', context)

class CustomLoginView(LoginView):
    def get_success_url(self):
        return '/participant/dashboard/'
    
