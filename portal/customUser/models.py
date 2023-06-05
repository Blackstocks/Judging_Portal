from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

class CustomUser(AbstractUser):
    is_judge = models.BooleanField('judge status', blank=True, default=False)
    is_participant = models.BooleanField('participant status', blank=True, default=False)

class Participant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    ppt_link = models.URLField(blank=True, max_length=1000)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.user.is_participant:
            super().save(*args, **kwargs)
        else:
            raise ValueError("Only participants are allowed.")

class Judge(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.user.is_judge:
            super().save(*args, **kwargs)
        else:
            raise ValueError("Only judges are allowed.")
