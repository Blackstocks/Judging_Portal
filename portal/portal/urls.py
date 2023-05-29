from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from customUser import views as user_views
from customUser.decorators import unauthenticated_user, judge_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    
    path('judge/', include('dashboardJudge.urls'), name="judge"),

    path('logout/', auth_views.LogoutView.as_view(template_name='customUser/mainpage.html'), name='logout'),
    
    path('accounts/login/', user_views.redirectuser , name='redirectuser'),
]
