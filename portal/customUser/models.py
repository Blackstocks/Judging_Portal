from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings

class customUser(AbstractUser):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
   is_judge = models.BooleanField('judge status',null=True, blank=True, default=False)
   is_participant = models.BooleanField('particpant status',null=True, blank=True, default=False)


class participant(models.Model):
    user = models.OneToOneField(customUser, on_delete=models.CASCADE, primary_key=True)
    
