from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from customUser.decorators import judge_required
from django.conf import settings

@judge_required
@login_required
def dashboard(request):
    return render(request, 'dashboardJudge/dashboard.html')

@judge_required
@login_required
def judge(request):
    pdf_file_path = f"{settings.BASE_DIR}/documents/participant1/sample.pdf"
    return render(request, 'dashboardJudge/judging.html', {'pdf_file_path': pdf_file_path})

@judge_required
@login_required
def leaderboard(request):
    return render(request, 'dashboardJudge/leaderboard.html')

