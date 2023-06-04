from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
import os

class customUser(AbstractUser):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
   is_judge = models.BooleanField('judge status',null=True, blank=True, default=False)
   is_participant = models.BooleanField('particpant status',null=True, blank=True, default=False)

def user_directory_path(instance, filename):
    # Get the current username
    username = instance.user.username

    # Return the file path
    return os.path.join('documents', username, filename)

class participant(models.Model):
   user = models.OneToOneField(customUser, on_delete=models.CASCADE, primary_key=True)
   data = models.JSONField(null=True, blank=True)
   ppt = models.FileField(null=True, blank=True, upload_to= user_directory_path)

   def __str__(self):
        return self.user.username

   def save(self, *args, **kwargs):
        if self.user.is_participant:
            super().save(*args, **kwargs)
        else:
            raise ValueError("Only participants are allowed.")
        
   def delete_ppt(self):
        if self.ppt:
            # Delete the file from storage
            if os.path.isfile(self.ppt.path):
                os.remove(self.ppt.path)
            # Clear the field
            self.ppt.delete()

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
        

    
