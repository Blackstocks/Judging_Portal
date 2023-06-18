from django.contrib import admin
from django.urls import include, path
from . import views
from customUser import views as user_views
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from customUser.decorators import unauthenticated_user, judge_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard, name="judge_dashboard"),
    path('judging/<str:participant_username>/', views.judge, name='judge_judge'),
    path('leaderboard', views.leaderboard, name='judge_leaderboard'),
    path('participants', views.participants, name='judge_participants'),

    path('register/', user_views.register, name='judge_register'),
    path('verify/', unauthenticated_user(user_views.VerifyOTP), name='judge_verify'),

    path('login/', unauthenticated_user(auth_views.LoginView.as_view(template_name='customUser/login.html')), name='judge_login'),

]

# Add this pattern to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
