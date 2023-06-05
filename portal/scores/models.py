from django.db import models
from customUser.models import CustomUser, Participant, Judge
from jsonfield import JSONField
from django.utils import timezone

class Score(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True)
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE, null=True)
    parameters = JSONField(null=True, default={})

    class Meta:
        unique_together = (('participant', 'judge'),)

    def __str__(self):
        return f"{self.participant}, {self.judge}"