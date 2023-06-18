from django.contrib import admin
from django import forms
from .models import Score

class ScoreAdmin(admin.ModelAdmin):
    class Meta:
        model = Score
        fields = '__all__'

admin.site.register(Score, ScoreAdmin)
# Register your models here.
