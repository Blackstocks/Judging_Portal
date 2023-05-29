from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from customUser.decorators import judge_required

@judge_required
@login_required
def dashboard(request):
    return render(request, 'dashboardJudge/dashboard.html')

@judge_required
@login_required
def judge(request):
    return render(request, 'dashboardJudge/judging.html')

