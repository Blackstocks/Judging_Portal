from django.contrib import admin
from django.urls import include, path
from . import views
from customUser import views as user_views
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from customUser.decorators import unauthenticated_user, judge_required

urlpatterns = [
    path('dashboard/', views.dashboard, name="judge_dashboard"),
    path('judging', views.judge, name='judge_judge'),
    path('leaderboard', views.leaderboard, name='judge_leaderboard'),

    path('register/', user_views.register, name='judge_register'),
    path('verify/', unauthenticated_user(user_views.VerifyOTP), name='judge_verify'),

    path('login/', unauthenticated_user(auth_views.LoginView.as_view(template_name='customUser/login.html')), name='judge_login'),

]