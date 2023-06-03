from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class customUser(AbstractUser):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
   is_judge = models.BooleanField('judge status',null=True, blank=True, default=False)
   is_participant = models.BooleanField('particpant status',null=True, blank=True, default=False)


class participant(models.Model):
   user = models.OneToOneField(customUser, on_delete=models.CASCADE, primary_key=True)
   data = models.JSONField(null=True, blank=True)

   def __str__(self):
        return self.user.username

   def save(self, *args, **kwargs):
        if self.user.is_participant:
            super().save(*args, **kwargs)
        else:
            raise ValueError("Only participants are allowed.")

class judge(models.Model):
   user = models.OneToOneField(customUser, on_delete=models.CASCADE, primary_key=True)
   data = models.JSONField(null=True, blank=True)

   def __str__(self):
        return self.user.username

   def save(self, *args, **kwargs):
        if self.user.is_judge:
            super().save(*args, **kwargs)
        else:
            raise ValueError("Only judges are allowed.")

    
